from django.db import models

# Create your models here.
class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30,unique=True)