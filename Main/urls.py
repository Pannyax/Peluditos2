from django.contrib import admin
from django.urls import path, include
from .views import addproductos, carro, index, login, contacto, ofertas, productos, razagatos, razaperros, registro, validarUsuario, guardarProducto, eliminarProducto, buscarProducto, guardarProductoModificado

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
    path('addproductos', addproductos),
    path('guardarProducto/', guardarProducto),
    path('guardarProductoCambiado/', guardarProductoModificado),
    path('eliminarProducto/<p_idProducto>', eliminarProducto),
    path('modificarProducto/<p_idProducto>', buscarProducto),
]