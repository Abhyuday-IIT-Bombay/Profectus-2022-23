from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Account(models.Model):
    name = models.CharField( max_length=50, default = "")
    email = models.EmailField( max_length=254 , default="")
    contact = PhoneNumberField()
    # resfile = models.FileField(upload_to='resume/pdfs/' , default="")   

    def __str__(self):
        return self.name

class Resume(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='resume/pdfs/')
    
    def __str__(self):
        return self.name

class Make_Resume(models.Model):
    fname = models.CharField( max_length=100)
    lname = models.CharField( max_length=100)
    email = models.EmailField( max_length=254)
    loc1 = models.CharField( max_length=500)
    loc2 = models.CharField( max_length=500)
    seducation = models.CharField( max_length=1000)
    sseducation = models.CharField( max_length=1000)
    graduation = models.CharField( max_length=1000)
    por = models.CharField( max_length=2000)
    course = models.CharField( max_length=2000)
    project = models.CharField( max_length=2000)
    skill = models.CharField( max_length=500)
    blog = models.CharField( max_length=500)
    github = models.CharField( max_length=500)
    other = models.CharField( max_length=500)

    def __str__(self):
        return self.fname
    










    
     