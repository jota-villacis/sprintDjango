from django import forms
from django.db.models import fields


class SolicitudContactoForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput)
    reclamo=forms.CharField(widget=forms.Textarea)