from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from users.managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    image = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=20)
    password = models.CharField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    ballance = models.DecimalField(decimal_places=2, max_digits=12)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)

    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["birth_date", ]

    def __str__(self):
        return f"{self.username}"


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return f"{self.user.username}"
