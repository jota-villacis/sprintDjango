from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from .models import User

class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            customer=User.objects.filter(email=username, password=password).get()
            return customer
        except:
            return None


    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
