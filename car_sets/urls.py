"""
URL configuration for car_sets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cars.views import home_view, cars_create_view, cars_list_view, car_update_view, car_detail_view
from django.conf.urls.static import static
from django.conf import settings
from users.views import register_view, login_view, logout_view, profile_view

user_patterns = [
    path("register/", register_view),
    path("login/", login_view),
    path("logout/", logout_view),
    path("profile/", profile_view)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view),
    path("vehicles/create", cars_create_view),
    path("vehicles/<int:pk>/update/", car_update_view),
    path('vehicles/', cars_list_view),
    path("vehicles/<int:car_id>/", car_detail_view),
] + user_patterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



