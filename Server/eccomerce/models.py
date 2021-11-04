from django.db import models

# Create your models here.

class User(models.Model):
    id=models.AutoField(primary_key=True)
    rut=models.CharField(max_length=15, unique=True, null=False)
    name=models.CharField(max_length=30, null=False)
    last_name=models.CharField(max_length=40, null=False)
    email=models.EmailField(max_length=100, null=False)
    phone_number=models.CharField(max_length=20, null=False)
    passwd=models.CharField(max_length=100, null=False)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=80, null=False)
    description=models.CharField(max_length=1000, null=False)
    unit_price=models.IntegerField()


