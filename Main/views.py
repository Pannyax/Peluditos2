from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Foto, Producto, Usuario, Contacto

# Create your views here.

def index(request):
    productos = Producto.objects.all()
    datos = {'productos': productos} #par ordenado de atributo y valor que se van a pasar a la vista
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

def addproductos(request):
    productos = Producto.objects.all()
    datos = {'productos': productos}
    return render(request, 'addproductos.html', datos)

def validarUsuario(request):
    v_email=request.POST.get('email')
    v_password=request.POST.get('password')

    usu=Usuario.objects.get(email=v_email, password=v_password)

    try:
        if usu:
            request.session['usuario'] =v_email
            return redirect('/index')
    
    except:
        return redirect('/index')

def guardarProducto(request):

    v_idproducto=request.POST.get('idproducto')
    v_nomproducto=request.POST.get('nombre')
    v_imgproducto=request.POST.get('imagen')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    nuevo=Producto()
    nuevo.idProducto=v_idproducto
    nuevo.nombreProducto=v_nomproducto
    nuevo.imagenProducto=v_imgproducto
    nuevo.stockProducto=v_stockproducto
    nuevo.precioProducto=v_preproducto

    Producto.save(nuevo)

    return redirect('/addproductos')

def eliminarProducto(request, p_idProducto):
    buscando=Producto.objects.get(idProducto=p_idProducto)
    if(buscando):
        Producto.delete(buscando)
        return redirect('/addproductos')

def buscarProducto(request, p_idProducto):
    buscando=Producto.objects.get(idProducto=p_idProducto)
    datos={'producto': buscando}
    return render(request, 'modificar.html', datos)

def guardarProductoModificado(request):
    v_idproducto=request.POST.get('idproducto')
    v_nomproducto=request.POST.get('nombre')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    buscando=Producto.objects.get(idProducto=v_idproducto)

    if(buscando):
        buscando.nombreProducto=v_nomproducto
        buscando.stockProducto=v_stockproducto
        buscando.precioProducto=v_preproducto

        Producto.save(buscando)
        return redirect('/addproductos')