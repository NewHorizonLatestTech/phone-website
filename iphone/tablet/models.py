from django.db import models

# Create your models here.
class person(models.Model):
        name = models.CharField(max_length=50,default="")
        age = models.IntegerField()
        password = models.CharField(max_length=50,default="")
        class_school = models.IntegerField()
        section = models.IntegerField()
        school_name = models.CharField(max_length=50,default="")
        father_name = models.CharField(max_length=50,default="")
        cnic = models.CharField(max_length=50,default="") 
        photo = models.ImageField(upload_to="myimage",default="")
        def __str__(self):
            return self.name
 
# help for me to sending data to models.py to forms.html show page
# name        
# age         
# password    
# class_school
# section     
# school_name 
# father_name 
# cnic        