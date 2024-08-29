from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    power_level = models.IntegerField()

    def __str__(self):
        return self.name
