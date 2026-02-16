from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from cars.models import Car

def author_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs["car_id"])

        if request.user != car.author:
            return HttpResponseForbidden("Not allowed U are not the owner")

        return view_func(request, *args, **kwargs)

    return wrapper
