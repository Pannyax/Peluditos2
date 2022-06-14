from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Foto, Producto, Usuario, Contacto

# Create your views here.

def index(request):
    fotos = Foto.objects.all()
    datos = {'fotos': fotos} #par ordenado de atributo y valor que se van a pasar a la vista
    return render(request, 'index.html', datos)

def carro(request):
    return render(request, 'carro.html')

def login(request):
    usuarios = Usuario.objects.all()
    datos = {'usuarios': usuarios}
    return render(request, 'login.html', datos)

def contacto(request):
    contactos = Contacto.objects.all()
    datos = {'contactos': contactos} #par ordenado de atributo y valor que se van a pasar a la vista
    return render(request, 'contacto.html', datos)

def ofertas(request):
    return render(request, 'ofertas.html')

def productos(request):
    productos = Producto.objects.all()
    datos = {'productos': productos}
    return render(request, 'productos.html', datos)

def razagatos(request):
    return render(request, 'razagatos.html')

def razaperros(request):
    return render(request, 'razaperros.html')

def registro(request):
    return render(request, 'registro.html')

def album(request):
    return render(request, 'album.html')

def validarUsuario(request):
    v_email=request.POST.get('email')
    v_password=request.POST.get('password')

    usu=Usuario.objects.get(email=v_email, password=v_password)

    if usu:
        request.session['usuario'] =v_email
        return redirect('index')

    return HTTPResponse('Hola tu email es:' + v_email)