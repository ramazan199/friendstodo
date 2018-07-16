from django.contrib import admin

# Register your models here.
from .models import RestaurantLocation, Todo

admin.site.register(RestaurantLocation)
admin.site.register(Todo)