from urllib import request
from django.shortcuts import render
from .models import *
from users.models import *
# Create your views here.

def dashboard(request):
    category=[]
    for cat in Profile.category:
        category.append(cat)
    print(category)

    return render(request, "dashboard.html")