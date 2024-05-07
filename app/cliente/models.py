from django.db import models


class Programmer(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)