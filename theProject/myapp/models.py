from django.db import models


# Create your models here.
class Projects(models.Model):
    pname=models.CharField(max_length=20,verbose_name="Name of the Project")
    pdesc=models.CharField(max_length=100,verbose_name="Description of the Project")
    pimage=models.ImageField(upload_to="project_images")
    price=models.IntegerField()
    
    def __str__(self):
        return self.pname
    
class Services(models.Model):
    sname=models.CharField(max_length=20,verbose_name="NAme of the Service")
    