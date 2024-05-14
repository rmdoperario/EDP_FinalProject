from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    COURSES = (
        ("BS CS", "BS-CS"),
        ("BS DS", "BS-DS"),
        ("BS IS", "BS-IS"),
        ("BS IT", "BS-IT"),
    )
    course = models.CharField(max_length=5, choices=COURSES)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
