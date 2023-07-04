from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, null=True, blank=True)
    profile_img = models.ImageField(blank=True, upload_to='images', default='images/p1.jpeg')
    about_me = models.TextField(max_length=5000, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
 
class Resume(models.Model):
    resume = models.FileField(upload_to='resume')   
    
    
class Education(models.Model):
    type = models.CharField(max_length=10,null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    university  = models.CharField(max_length=200, null=True )    
    city = models.CharField(max_length=200, null=True, blank=True)
    course = models.CharField(max_length=200,null=True)
    marks = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return  self.type
    
class Languages(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name    
    
    
class Skills(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Projects(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=200, null=True)
    image =  models.ImageField(upload_to='images/project', null=True, blank=True, verbose_name="image(300x400)")   
    link = models.CharField(max_length=5000, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    mail = models.CharField(max_length=50,null= True)
    phone = models.CharField(max_length=15, null=True) 
    message = models.TextField(max_length=500,null=True)   
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)+ '  --------------------------------------------------------------------->  ' + str(self.time)
    