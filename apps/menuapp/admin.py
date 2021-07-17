from django.contrib import admin
from .models import Order, Option, Menu

# Register your models here.
admin.site.register(Order)
admin.site.register(Option)
admin.site.register(Menu)