from django.db import models


# Create your models here.
class Projects(models.Model):
    ptype=models.CharField(max_length=50,verbose_name="Project Type")
    pname=models.CharField(max_length=200,verbose_name="Project Name")
    pimage=models.ImageField(upload_to='image')
    
    def __str__(self):
        return self.pname