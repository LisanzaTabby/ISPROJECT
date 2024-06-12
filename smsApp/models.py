from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
class Trustee(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    Student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
class School(models.Model):
    LEVEL = (
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('Both Primary&Secondary', 'Both Primary&Secondary'),
        ('Tertiary', 'Tertiary'),
    )
    LOCATION = (
        ('Nairobi', 'Nairobi'),
        ('Kisumu', 'Kisumu'),
        ('Mombasa', 'Mombasa'),
        ('Marsabit', 'Marsabit'),
        ('Kajiado', 'Kajiado'),
        ('Lamu', 'Lamu'),
        ('Kilifi', 'Kilifi'),
        ('Kakamega', 'Kakamega'),
        ('Kisii', 'Kisii'),
        ('Turkana', 'Turkana'),
    )
    Student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    schoolname = models.CharField(max_length=200)
    Level = models.CharField(max_length=100, choices=LEVEL)
    Location = models.CharField(max_length=100,choices=LOCATION)
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.schoolname}'


