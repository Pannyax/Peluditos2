from django.contrib import admin
from .models import Categoria, Producto, Foto

# Register your models here.
# Permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Foto)
