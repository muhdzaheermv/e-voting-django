from django.db import models

# Create your models here.

class ElectionOfficer(models.Model):
    register_no = models.IntegerField()
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
