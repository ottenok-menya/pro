from django.contrib import admin
from .models import Furniture
from .models import Category

admin.site.register(Furniture)
admin.site.register(Category)