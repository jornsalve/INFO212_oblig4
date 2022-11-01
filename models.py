from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.Charfield(max_length = 50)
    carmodel = models.Charfield(max_length = 50)

    def __str__(self):
        return self.make + ''+ + self.carmodel
