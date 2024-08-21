from django.db import models

# Create your models here.


class Student_model(models.Model):
    Sname=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Reenterpassword=models.CharField(max_length=100)
    Email=models.EmailField()
    ReenterEmail=models.EmailField()
    def __str__(self):
        return self.Sname




    
