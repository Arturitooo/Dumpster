from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):

        return f"The patient name is: {self.first_name} nad he is {self.age} years old"