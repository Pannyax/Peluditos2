from django.urls import URLPattern, path
from .views import traerProductos

urlpatterns= [
    path('traerProductos', traerProductos, name='traer_productos'),
]