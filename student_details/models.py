from django.db import models
from datetime import datetime

# Courses
class Courses(models.Model):
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.course


# ClassName
class ClassName(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# Student
class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    course_enroll = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


