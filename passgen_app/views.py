from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse as hr
import random

# Create your views here.
def home(request):
    return render(request,'passgen_app/home.html' )

def page1(request):
    characters =list('abcdefghijklmnopqrstuvwxyz')
    thepassword=''
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialcharacters'):
        characters.extend(list('!@#$%^&*()_'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length=int(request.GET.get('length',8))

    if length == None:
        return render(request,'generator/home.html')

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,'passgen_app/generator.html',{'password':thepassword})
