from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    age = models.CharField(max_length=40)

class Employee(models.Model):
    EmpName = models.CharField(max_length=40)
    Emprole = models.CharField(max_length=40)
    EmpSal= models.IntegerField()

class Student(models.Model):
    name=models.CharField(max_length=64)
    rollno= models.IntegerField()
    marks= models.IntegerField()
    age = models.IntegerField()


#django new api
class Cricketer(models.Model):
    name=models.CharField(max_length=64)
    role= models.CharField(max_length=64)
    jersyno= models.IntegerField()
    favshort = models.CharField(max_length=64)