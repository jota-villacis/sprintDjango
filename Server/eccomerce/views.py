from django import forms
from django.shortcuts import render
from .models import User
from .forms import SolicitudContactoForm

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
    return render(request, 'eccomerce/contacto.html')

def solicitarContacto(request):
    datos=request.POST
    email=datos["email"]
    reclamo=datos["reclamo"]
    print(email,reclamo)
    #name=datos["nameData"]
    #last_name=datos["lastNameData"]
    #city=datos["cityData"]
    #email=datos["emailData"]
    #description=datos["descriptionData"]
    #print(name,last_name,email,city,description)
    return render(request, 'eccomerce/contacto.html', {"mensaje":"Datos Recibidos","email":email,"reclamo":reclamo})

def contacto2(request):
    if request.method == "POST":
        form=SolicitudContactoForm(data=request.POST)
        email=form["email"]
        reclamo=form["reclamo"]
        return render(request, 'eccomerce/contactoDjango.html',{"respuesta":"ok!"})
    else:
        form = SolicitudContactoForm()
        return render(request, 'eccomerce/contactoDjango.html', {"form":form})