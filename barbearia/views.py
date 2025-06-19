from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def my_view(request):
    return HttpResponse("Hello, world! This is my view.")

def sobre(request):
    return render(request, 'barbearia/sobre.html')

def home(request):
    return render(request, 'home/home.html')
