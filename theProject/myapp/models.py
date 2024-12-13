from django.db import models


# Create your models here.
class Project(models.Model):
    pimage=models.ImageField(upload_to='project_images')
    pname=models.CharField(max_length=30,verbose_name="Project Name")
    desc=models.CharField(max_length=100,verbose_name="Project Description")
    title=models.CharField(max_length=20,verbose_name="title")
    
    # def __str__(self):
    #     return self.pname