from django.db import models
import datetime as dt

# Create your models here.
class Familiar(models.Model):
    first_name = models.CharField(max_length=14, default="")
    last_name = models.CharField(max_length=14, default="")
    age = models.IntegerField(default=0)
    #birth_date = models.DateField(default=dt.date(1970,1,1))
    address = models.CharField(max_length=255, default="")
    is_alive = models.BooleanField(default=True)
    #f_nacimiento = models.DateField()

    def __str__(self):
        return f"Nombre: \"{self.first_name} {self.last_name}\", Edad: {self.age}"


