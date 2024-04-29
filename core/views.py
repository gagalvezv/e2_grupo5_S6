from django.shortcuts import render, redirect
from .models import Usuario, Inventario, Categoria
from .forms import UsuarioForm
from django.contrib import messages
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import InventarioSerializer

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def iniciarsesion(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')
        print("Datos del form", username,password)
        #return render(request, 'core/registro.html')
        usuarioBD = Usuario.objects.filter(username=username).first()
        if usuarioBD is not None:
            if usuarioBD.password == password:
                if usuarioBD.perfil == 1:
                    return render(request, 'core/index.html')
                if usuarioBD.perfil == 2:
                    print("Home usuario")
                    return render(request, 'core/index.html')
                else:
                    print("No se encontro perfil")
                    return render(request, 'core/iniciarsesion.html')
            else:
                print("Password incorrecta")
                return render(request, 'core/iniciarsesion.html')
        else:
            print("Usuario no existe")
            return render(request, 'core/iniciarsesion.html')
    else:
        return render(request, 'core/iniciarsesion.html')

def modificarperfil(request):
    return render(request, 'core/modificarperfil.html')

def deportivas(request):
    categoriaDeportivas = Categoria.objects.get(nombre_categoria = 'Deportivas')
    inventarios = Inventario.objects.filter(categoria=categoriaDeportivas)
    
    datos = {  
        'inventario' : inventarios
    }
    print(datos)
    return render(request, 'core/deportivas.html', datos)

def casuales(request):
    categoriaCasuales = Categoria.objects.get(nombre_categoria = 'Casuales')
    inventarios = Inventario.objects.filter(categoria=categoriaCasuales)
    
    datos = {  
        'inventario' : inventarios
    }
    print(datos)
    return render(request, 'core/casuales.html', datos)

def descanso(request):
    categoriaDescanso = Categoria.objects.get(nombre_categoria = 'Descanso')
    inventarios = Inventario.objects.filter(categoria=categoriaDescanso)
    
    datos = {  
        'inventario' : inventarios
    }
    print(datos)
    return render(request, 'core/descanso.html', datos)

def carro(request):
    return render(request, 'core/carritodecompras.html')

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            messages.success(request, "El producto fue creado correctamente")
            form.save()
            
    else:
        form = UsuarioForm()
    return render(request, 'core/registro.html', {'form' : form})

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_inventario(request):
    if request.method == 'GET':
        inventario = Inventario.objects.all()
        serializer = InventarioSerializer(inventario, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InventarioSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])        
def vista_inventario(request,id_inventario):
    try:
        inventario = Inventario.objects.get(id_inventario=id_inventario)
    except Inventario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = InventarioSerializer(inventario)
        return Response(serializer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = InventarioSerializer(inventario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)\
                
    elif request.method == 'DELETE':
        inventario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
def form_api(request):
    return render(request, 'core/form_api.html') 




