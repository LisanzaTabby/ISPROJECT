from django.db import models

# Create your models here.
class student(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    


