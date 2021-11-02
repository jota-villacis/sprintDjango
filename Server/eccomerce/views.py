from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'eccomerce/index.html')

def productos(request):
    return render(request, 'eccomerce/productos.html')

def pago(request):
    return render(request, 'eccomerce/pago.html')