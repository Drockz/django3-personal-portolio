from django.shortcuts import render
from .models import project

# Create your views here.
def home(request):
    Project= project.objects.all()
    return render(request,'portfolio_app/home.html',{'Projects':Project})
