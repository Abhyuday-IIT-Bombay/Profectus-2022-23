from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Account(models.Model):
    name = models.CharField( max_length=50, default = "")
    email = models.EmailField( max_length=254 , default="")
    contact = PhoneNumberField()
    roll = models.CharField( max_length=50, default = "")
    department = models.CharField( max_length=50, default = "")
    year = models.CharField( max_length=50, default = "")
    # resfile = models.FileField(upload_to='resume/pdfs/' , default="")   

    def __str__(self):
        return self.name

class Resume(models.Model):
    Name = models.CharField(max_length=100)
    Resume = models.FileField(upload_to='resume/pdfs/')
    
    def __str__(self):
        return self.name

class Make_Resume(models.Model):
    fname = models.CharField( max_length=100 ,default="")
    lname = models.CharField( max_length=100 ,default="")
    department = models.CharField( max_length=100 ,default="")
    roll = models.CharField( max_length=100 ,default="")
    year = models.CharField( max_length=100 ,default="")
    startyear = models.CharField( max_length=100 ,default="")
    endyear = models.CharField( max_length=100 ,default="")
    cpi = models.CharField( max_length=100 ,default="")
    board12 = models.CharField( max_length=100 ,default="")
    college = models.CharField( max_length=100 ,default="")
    year12 =models.CharField( max_length=100 ,default="")
    cpi12 = models.CharField( max_length=100 ,default="")
    board10 = models.CharField( max_length=100 ,default="")
    school = models.CharField( max_length=100 ,default="")
    year10 =models.CharField( max_length=100 ,default="")
    cpi10 = models.CharField( max_length=100 ,default="")
    ptitle1 = models.CharField( max_length=200 ,default="")
    p1start = models.CharField( max_length=100 ,default="")
    p1end = models.CharField( max_length=100 ,default="")
    p1info = models.CharField( max_length=1000 ,default="")
    ptitle2 = models.CharField( max_length=200 ,default="")
    p2start = models.CharField( max_length=100 ,default="")
    p2end = models.CharField( max_length=100 ,default="")
    p2info = models.CharField( max_length=1000 ,default="")
    ptitle3 = models.CharField( max_length=200 ,default="")
    p3start = models.CharField( max_length=100 ,default="")
    p3end = models.CharField( max_length=100 ,default="")
    p3info = models.CharField( max_length=1000 ,default="")
    proj1 = models.CharField( max_length=200 ,default="")
    proj1start = models.CharField( max_length=100 ,default="")
    proj1end = models.CharField( max_length=100 ,default="")
    proj1info = models.CharField( max_length=1000 ,default="")
    proj2 = models.CharField( max_length=200 ,default="")
    proj2start = models.CharField( max_length=100 ,default="")
    proj2end = models.CharField( max_length=100 ,default="")
    proj2info = models.CharField( max_length=1000 ,default="")
    proj3 = models.CharField( max_length=200 ,default="")
    proj3start = models.CharField( max_length=100 ,default="")
    proj3end = models.CharField( max_length=100 ,default="")
    proj3info = models.CharField( max_length=1000 ,default="")
    techskill = models.CharField( max_length=1000 ,default="")
    activity1start = models.CharField( max_length=100 ,default="")
    activity1end = models.CharField( max_length=100 ,default="")
    activity1info = models.CharField( max_length=1000 ,default="")
   
    activity2start = models.CharField( max_length=100 ,default="")
    activity2end = models.CharField( max_length=100 ,default="")
    activity2info = models.CharField( max_length=1000 ,default="")

    activity3start = models.CharField( max_length=100 ,default="")
    activity3end = models.CharField( max_length=100 ,default="")
    activity3info = models.CharField( max_length=1000 ,default="")
    def __str__(self):
        return self.fname
    

class Apply(models.Model):
    name = models.CharField( max_length=100 ,default="")
    roll = models.CharField( max_length=100 ,default="")
    pref1 = models.CharField( max_length=100 ,default="")
    pref2 = models.CharField( max_length=100 ,default="")
    pref3 = models.CharField( max_length=100 ,default="")


    
   










    
     