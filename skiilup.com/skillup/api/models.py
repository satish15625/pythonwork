from django.db import models

# Create your models here.

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    mobile = models.CharField(max_length=20)
    position = models.CharField(max_length=60)
    exprience = models.CharField(max_length=20)

    def __str__(self):
        return self.name