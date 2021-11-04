from django.http.request import validate_host
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index),
    path('productos/', views.productos),
    path('pago/', views.pago),
    path('usuarios/', views.usuarios),
    path('contacto/', views.contacto),
    path('solicitarContacto', views.solicitarContacto),
    path('contacto2/', views.contacto2)
]
