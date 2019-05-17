from django.db import models

class Employee(models.Model):
# Create your models here.
      eid=models.IntegerField()
      ename=models.CharField(max_length=10)
      esal=models.IntegerField()
