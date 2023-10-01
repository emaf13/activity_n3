from django.db import models
from datetime import datetime as dt

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    #f_nacimiento = models.DateField()

    def __str__(self):
        return f"Nombre: \"{self.nombre}\", Edad: {self.edad}"


