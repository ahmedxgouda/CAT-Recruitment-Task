from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, error_messages={'unique': 
        'A user with that email already exists.'})
    role = models.CharField(max_length=50, default='client')
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username
    