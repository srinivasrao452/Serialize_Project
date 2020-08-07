

from django.db import models

# from server to local

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=100)

    def __str__(self):
        return self.ename
