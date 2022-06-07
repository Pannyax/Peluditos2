from django.shortcuts import render
from .models import Foto

# Create your views here.

def index(request):
    fotos = Foto.objects.all()
    datos = {'fotos': fotos} #par ordenado de atributo y valor que se van a pasar a la vista
    return render(request, 'index.html', datos)

def carro(request):
    return render(request, 'carro.html')

def login(request):
    return render(request, 'login.html')

def contacto(request):
    return render(request, 'contacto.html')

def ofertas(request):
    return render(request, 'ofertas.html')

def productos(request):
    return render(request, 'productos.html')

def razagatos(request):
    return render(request, 'razagatos.html')

def razaperros(request):
    return render(request, 'razaperros.html')

def registro(request):
    return render(request, 'registro.html')