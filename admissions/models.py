

from django.db import models
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    classname = models.IntegerField(default=1)
    contact = models.CharField(max_length=50)


class Teacher(models.Model):
    name  = models.CharField(max_length=100)
    exp = models.IntegerField()
    subject = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('getteacher')