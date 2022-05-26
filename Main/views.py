from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def carro(request):
    return render(request, 'carro.html')

def login(request):
    return render(request, 'login.html')
    