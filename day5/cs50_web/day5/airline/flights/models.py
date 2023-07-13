from typing import Any
from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"



class Flight(models.Model):
    # origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name="departures")
    #if you delete airport from airport table delete it from this table too
    #related names can be different for each key even it s connected with same table

    # destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name = "arrivals")
    #

    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

#migration in order to update database to have the new models


class Passenger(models.Model):
    first = models.CharField(max_length = 64)
    last = models.CharField(max_length = 64)
    flights = models.ManyToManyField(Flight, blank = True, related_name = "passengers")

    def __str__(self):
        return f"{self.first} {self.last}"