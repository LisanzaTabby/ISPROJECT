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
    


