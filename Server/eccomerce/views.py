from django import forms
from django.shortcuts import redirect, render
from .models import User
from .forms import LoginForm, SolicitudContactoForm, UserForm 
from django.contrib.auth import authenticate, login as auth_login

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

def solicitar_contacto(request):
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

def contacto_second(request):
    if request.method == "POST":
        form=SolicitudContactoForm(data=request.POST)
        email=form["email"]
        reclamo=form["reclamo"]
        return render(request, 'eccomerce/contactoDjango.html',{"respuesta":"ok!"})
    else:
        form = SolicitudContactoForm()
        return render(request, 'eccomerce/contactoDjango.html', {"form":form})


# def contacto_second(request, *args, **kwargs):
#     form=SolicitudContactoForm(request.POST or None)
#     if form.is_valid():
#         print(request.POST)
#         print(form.cleaned_data)
#     return render(request, "eccomerce/contactoDjango.html", {"forms": form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            #Guardado en DB
            usuario.save()
        return redirect('/usuarios/')
    else:
        form = UserForm()
        return render(request, 'eccomerce/crearCliente.html', {"form": form})

def login(request):
    if request.method == 'POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data["nombre"]
            passwd=form.cleaned_data["password"]
            user=authenticate(request,username=usuario,password=passwd)
            if user is not None:
                auth_login(request,user)
        return render(request,'eccomerce/welcome.html',{'user':user})
    else:
        form=LoginForm()
        return render(request,'eccomerce/login.html',{'form':form})
