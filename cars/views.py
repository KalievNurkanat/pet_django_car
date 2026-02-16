from django.shortcuts import render, HttpResponse, redirect
from cars.forms import  CarForm, SearchForm, CarSellForm
from cars.models import Car
from django.contrib.auth.decorators import login_required
from common.validators import validate_age, validate_ballance
from common.permissions import author_required
from django.shortcuts import get_object_or_404
from cars.tasks import send_via_email

# Create your views here.
def home_view(request):
    if request.method == "GET":
        return render(request, "base.html")
    

@login_required(login_url="/users/login/")
def cars_create_view(request):
    user = request.user
    if request.method == "GET":
        form = CarForm()
        return render(request, "vehicles/cars_creation.html", context={"form":form})
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)

        if not form.is_valid():
           return render(request, "vehicles/cars_creation.html", context={"form":form})
       
        validate_age(user)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("/vehicles")
    

@login_required(login_url="/users/login/")
def cars_list_view(request):
    form = SearchForm()
    cars = Car.objects.all()
    limit = 3
    if request.method == "GET":
        query_params = request.GET
        search = query_params.get("search")
        type_id = query_params.get("type_id")
        page = int(query_params.get("page", 1))

        if search:
            cars = cars.filter(mark__icontains=search)

        if type_id:
            cars = cars.filter(type_id=type_id)  
        
        if page:
            max_pages = cars.count() / limit
            
            if round(max_pages) < max_pages:
                max_pages = round(max_pages) + 1

            else:
                max_pages = round(max_pages)
                start = (page - 1) * limit
                end = page * limit
                cars = cars[start:end]
        
        return render(request, "vehicles/cars_list.html", 
                      context={"cars":cars, "form":form, 
                               "max_pages":range(1, max_pages + 1)})


@login_required(login_url="/users/login/")
def car_detail_view(request, car_id):
    if request.method == "GET":
        cars = get_object_or_404(Car, id=car_id)
        return render(request, "vehicles/car_detail.html", context={"cars":cars})
    

@login_required(login_url="users/login/")
def sales_page_view(request):
    cars = Car.objects.filter(is_for_sale=True)
    limit = 5
    form = SearchForm()
    if request.method == "GET":
        query_params = request.GET
        search = query_params.get("search")
        type_id = query_params.get("type_id")
        page = int(query_params.get("page", 1))
        if search:
            cars = cars.filter(mark__icontains=search)

        if type_id:
            cars = cars.filter(type_id=type_id)  
        
        if page:
            max_pages = cars.count() / limit
            
            if round(max_pages) < max_pages:
                max_pages = round(max_pages) + 1

            else:
                max_pages = round(max_pages)
                start = (page - 1) * limit
                end = page * limit
                cars = cars[start:end]
        return render(request, "vehicles/sale_page.html", context={"cars":cars, "form":form, 
                               "max_pages":range(1, max_pages + 1)})
    
@login_required(login_url="/users/login/")
def payment_view(request, car_id):
    car = Car.objects.get(id = car_id)
    if request.method == "GET":
        return render(request, "vehicles/payment.html", context={"car":car})
    if request.method == "POST":
        if car.author == request.user:
            return redirect("/users/profile/")

        try:
            validate_ballance(request.user, car)
        except ValueError:
            return HttpResponse("Not enough balance")
        
        send_via_email(request.user, car)
        car.author = request.user
        car.is_for_sale = False
        car.save()
        return redirect("/users/profile/")
    

@login_required(login_url="/users/login/")
@author_required
def sell_car_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "GET": 
        form = CarSellForm(instance=car)
        return render(request, "vehicles/car_sale.html", context={"form":form})
    if request.method == "POST":
        form = CarSellForm(request.POST, instance=car)

        if not form.is_valid():
           return render(request, "vehicles/car_sale.html", context={"form":form})
        
        sale = form.save(commit=False)
        sale.is_for_sale = True
        sale.save()
        return redirect("/vehicles")


@login_required(login_url="/users/login/")
def car_update_view(request, pk):
    car = Car.objects.get(id=pk, author=request.user)
    if request.method == "GET":
        form = CarForm(instance=car)
        return render(request, "vehicles/car_update.html", context={"form":form})
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if not form.is_valid():
           return render(request, "vehicles/car_update.html", context={"form":form})
        form.save()
        return redirect('/users/profile/')
  