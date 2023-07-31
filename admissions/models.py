from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    classname = models.IntegerField(default=1)
    contact = models.CharField(max_length=50)
