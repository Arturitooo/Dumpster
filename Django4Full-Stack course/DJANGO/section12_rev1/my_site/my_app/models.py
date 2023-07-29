from django.db import models

# Create your models here.
class Car(models.Model):
    #pk
    brand = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.pk} | {self.brand} - {self.year}"