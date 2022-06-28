from pyexpat import model
from django.db import models

class Gerente(models.Model):

    nombre = models.CharField(max_length=30)
    legajo = models.IntegerField(max_length=30)
    fecha_ingreso = models.DateField()

class Vendedor(models.Model):

    nombre = models.CharField(max_length=30)
    legajo = models.IntegerField(max_length=30)
    fecha_ingreso = models.DateField()

class Expedicionista(models.Model):

    nombre = models.CharField(max_length=30)
    legajo = models.IntegerField(max_length=30)
    fecha_ingreso = models.DateField()    