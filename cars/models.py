from django.db import models
from django.conf import settings

# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.type}"


class Car(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    mark = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=100)
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    is_for_sale = models.BooleanField(default=False)
  

    def __str__(self):
        return f"{self.mark}"
    