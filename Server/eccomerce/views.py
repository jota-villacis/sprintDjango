from django.shortcuts import render
from .models import User

# Create your views here.

def index(request):
    return render(request, 'eccomerce/index.html')

def productos(request):
    return render(request, 'eccomerce/productos.html')

def pago(request):
    return render(request, 'eccomerce/pago.html')

def usuarios(request):
    user=User.objects.all()
    return render(request, 'eccomerce/usuarios.html', {"datos":user})

def contacto(request):
    datos=request.GET
    name=datos["firstName"]
    last_name=datos["lastName"]
    user_name=datos["userName"]
    city=datos["nameCity"]
    print(name,last_name,user_name,city)
    return render(request, 'eccomerce/contacto.html', {"mensaje":"Datos Recibidos" })