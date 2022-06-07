from django.db import models

# Create your models here.

# Modelo para Categorias
class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de la Categoria')
    nombreCategoria =models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria


# Modelo para Producto
class Producto(models.Model):
    idProducto =models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombreProducto =models.CharField(max_length=50, verbose_name='Nombre del Producto')
    imagenProducto =models.CharField(max_length=150, verbose_name='Imagen del Producto')
    precioProducto =models.IntegerField(verbose_name='Precio del Producto')
    stockProducto =models.IntegerField(verbose_name='Stock del Producto')
    categoriaProducto =models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProducto

# Modelo para Fotos
class Foto(models.Model):
    idFoto = models.IntegerField(primary_key=True)
    nombreFoto = models.CharField(max_length=100)
    nombreArchivo = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=500)
    fechaPublicacion = models.DateField

    def __str__(self):
        return self.nombreFoto