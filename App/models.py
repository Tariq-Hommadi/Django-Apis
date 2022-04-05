from pyexpat import model
from django.db import models

# Create your models here.


class User(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=200)


class Task(models.Model):
    Id = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    task = models.CharField(max_length=200, default='task1')
    dueDate = models.DateField()
    status = models.CharField(max_length=200)
