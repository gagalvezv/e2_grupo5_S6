from django.shortcuts import render
from .models import Usuario

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

def registro(request):
    return render(request, 'core/registro.html')

#def registro(request):
    #return render(request, 'core/registro.html')

def modificarperfil(request):
    return render(request, 'core/modificarperfil.html')

def deportivas(request):
    return render(request, 'core/deportivas.html')

def casuales(request):
    return render(request, 'core/casuales.html')

def descanso(request):
    return render(request, 'core/descanso.html')

def carro(request):
    return render(request, 'core/carritodecompras.html')
