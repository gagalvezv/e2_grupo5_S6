from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('iniciarsesion/', views.iniciarsesion, name="iniciarsesion"),
    path('registro/', views.registro, name="registro"),
    path('perfil/', views.modificarperfil, name="modificarperfil"),
    path('deportivas/', views.deportivas, name="deportivas"),
    path('casuales/', views.casuales, name="casuales"),
    path('descanso/', views.descanso, name="descanso"),
    
]
