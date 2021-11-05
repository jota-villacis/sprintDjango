from django import forms
from django.db.models import fields
from django.forms.widgets import PasswordInput
from .models import Product, User


class SolicitudContactoForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput)
    reclamo=forms.CharField(widget=forms.Textarea)

class UserForm(forms.ModelForm):
    class Meta:      
        model=User
        fields=('id','rut','name','last_name','email','phone_number','passwd')

class ProducForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('id','name','unit_price','description')

class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)

class AppUserForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)




