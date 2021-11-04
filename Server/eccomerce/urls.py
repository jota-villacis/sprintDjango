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
    path('solicitar_contacto/', views.solicitar_contacto),
    path('contacto_second/', views.contacto_second),
    path('crea_cliente/', views.add_user),
    path('login/', views.login)
]
