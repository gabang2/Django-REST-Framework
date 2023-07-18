from django.db import models


# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class Class(models.Model):
    class_id = models.CharField(max_length=15, unique=True)
    students = models.ManyToManyField("Student")
    teacher = models.CharField(max_length=5)
