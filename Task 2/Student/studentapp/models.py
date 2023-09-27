from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    roll = models.IntegerField()
    address = models.TextField()
    mobile = models.CharField(max_length=75)