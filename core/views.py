from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def iniciarsesion(request):
    return render(request, 'core/iniciarsesion.html')

def registro(request):
    return render(request, 'core/registro.html')

def modificarperfil(request):
    return render(request, 'core/modificarperfil.html')

def deportivas(request):
    return render(request, 'core/deportivas.html')

def casuales(request):
    return render(request, 'core/casuales.html')

def descanso(request):
    return render(request, 'core/descanso.html')