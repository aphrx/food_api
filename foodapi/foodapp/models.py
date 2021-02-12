from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    calories = models.IntegerField()

    def __str__(self):
        return self.name