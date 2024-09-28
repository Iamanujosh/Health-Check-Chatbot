from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    medical_history = models.CharField(max_length=100) # If you're building a healthcare app

    def __str__(self):
        return self.name


# Create your models here.
