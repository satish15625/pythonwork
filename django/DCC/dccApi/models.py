from django.db import models
from datetime import datetime
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)



class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee" 

# models.py 
class UploadImages(models.Model): 
	name = models.CharField(max_length=50) 
	image_Img = models.ImageField(upload_to='images/')


