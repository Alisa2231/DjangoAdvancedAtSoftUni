from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)