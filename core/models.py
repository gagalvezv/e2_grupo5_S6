from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

#user admin kickstreetadmin pw: adminbbdd1

# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField(max_length=30, verbose_name='nombres', null=False)
    apellido = models.CharField(max_length=30, verbose_name='apellidos', null=False)
    rut = models.IntegerField(primary_key=True, verbose_name='rut')
    email = models.EmailField(max_length=60, verbose_name='email', null=False)
    password = models.CharField(max_length=20, verbose_name='password',null=True)
    
    
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name= 'id modelo')
    nombre_categoria = models.CharField(max_length=60, verbose_name='categoria')
    
    def __str__(self):
        return self.nombre_categoria
    
class Inventario(models.Model):
    id_inventario = models.IntegerField(primary_key=True, verbose_name= 'id inventario')
    modelo = models.CharField(max_length=30, verbose_name='modelo')
    talla = models.IntegerField(verbose_name='talla')
    valor = models.IntegerField(verbose_name='valor')
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to= 'inventario/', null=True, verbose_name='imagen del producto')
    
    def __str__(self):
        return self.modelo
    
