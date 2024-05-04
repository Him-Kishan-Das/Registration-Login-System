from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)