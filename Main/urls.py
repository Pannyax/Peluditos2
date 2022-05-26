from django.urls import path
from .views import carro, index, login

urlpatterns = [
    path('', index), 
    path('carro', carro),
    path('login', login)
]