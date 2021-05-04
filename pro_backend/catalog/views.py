from django.shortcuts import render
from .models import Furniture
from .models import Category

def home(request):
    categories = Category.objects.all()
    furnitures = Furniture.objects.all()
    return render(request, 'index.html', {'categories':categories, 'furnitures':furnitures})
