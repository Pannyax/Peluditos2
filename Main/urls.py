from django.urls import path
from .views import carro, index, login, contacto, ofertas, productos, razagatos, razaperros, registro, validarUsuario

urlpatterns = [
    path('', index),
    path('index', index), 
    path('carro', carro),
    path('login', login),
    path('contacto', contacto),
    path('ofertas', ofertas),
    path('razagatos', razagatos),
    path('razaperros', razaperros),
    path('productos', productos),
    path('registro', registro),
    path('validarUsuario', validarUsuario),
]