from django.shortcuts import render, redirect, HttpResponse
from users.forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from users.models import Profile
from cars.models import Car
from users.models import CustomUser


# Create your views here.
def register_view(request):
    if request.method == "GET":
       form = RegistrationForm()
       return render(request, "user/registrate.html", context={"form":form})
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if not form.is_valid():
           return render(request, "user/registrate.html", context={"form":form})
        try:
            form.cleaned_data.__delitem__("confirm_password")
            image = form.cleaned_data.pop("image")
            user = CustomUser.objects.create_user(
                **form.cleaned_data
            )
            if user:
                Profile.objects.create(user=user, image=image)
            return redirect("/")
        except Exception as x:
            return HttpResponse(f"Error {x}")


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "user/login.html", context={"form":form})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
           return render(request, "user/login.html", context={"form":form})
        user = authenticate(**form.cleaned_data)
        if not user:
            form.add_error(None, "Invalid password or username")
            return render(request, "user/login.html", context={"form":form})
        login(request, user)
        return redirect("/")
    

def logout_view(request):
    logout(request)
    return render(request, "base.html")


def profile_view(request):
    if request.method == "GET":
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
            cars = Car.objects.filter(author=user)
        except Exception:
            return HttpResponse("No profile found")
        
        return render(request, "user/profile.html", context={"profile":profile, "cars":cars})
    
