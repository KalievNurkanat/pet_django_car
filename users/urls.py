from django.urls import path
from users.views import register_view, login_view, logout_view, profile_view

urlpatterns = [
    path("register/", register_view),
    path("login/", login_view),
    path("logout/", logout_view),
    path("profile/", profile_view)
]