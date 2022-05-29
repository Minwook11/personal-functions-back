from django.db import models


class User(models.Model):
    account    = models.EmailField(max_length=128, unique=True)
    password   = models.CharField(max_length=256)
    name       = models.CharField(max_length=128, null=True)
    birthday   = models.DateTimeField(null=True)
    department = models.CharField(max_length=128, null=True)
    cellphone  = models.CharField(max_length=64, null=True)
    timestamp  = models.DateTimeField(auto_now_add=True)
    is_active  = models.BooleanField(default=False)
    is_admin   = models.BooleanField(default=False)
    barcode    = models.ImageField(null=True, upload_to="", blank=True)
