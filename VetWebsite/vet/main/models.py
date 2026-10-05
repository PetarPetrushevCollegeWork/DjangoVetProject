from django.contrib.auth.models import User
from django.db import models


class Booking(models.Model):
    ANIMALS = [("dog", "Dog"),
               ("cat", "Cat"),
               ("rabbit", "Rabbit"),
               ("other", "Other")
               ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100)
    animal = models.CharField(max_length=10, choices=ANIMALS)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet_name} ({self.animal}) on {self.date}"