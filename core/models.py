from django.db import models

#user admin kickstreetadmin pw: adminbbdd1

# Create your models here.
class Usuario(models.Model):
    run = models.IntegerField(primary_key=True, verbose_name='run')
    username = models.CharField(max_length=25, verbose_name='usuario')
    nombres = models.CharField(max_length=60, verbose_name='nombres')
    apellidos = models.CharField(max_length=60, verbose_name='apellidos')
    password = models.CharField(max_length=25, verbose_name='contraseña')
    perfil = models.IntegerField(null=True, blank=True, verbose_name='perfil')
    