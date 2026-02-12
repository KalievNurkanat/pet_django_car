from django.contrib import admin
from cars.models import Car, Type
# Register your models here.

@admin.register(Car)
class Admin(admin.ModelAdmin):
    list_display = ("mark", "type")
    list_editable = ("type",)

admin.site.register(Type)
