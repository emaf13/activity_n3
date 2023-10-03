from django.db import models
from datetime import date

# Create your models here.
class Familiar(models.Model):
    first_name = models.CharField(max_length=14, default="")
    last_name = models.CharField(max_length=14, default="")
    age = models.IntegerField(default=0)
    birth_date = models.DateField(default=date.today())
    address = models.CharField(max_length=255, default="")
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return f"\"{self.first_name} {self.last_name}\""


