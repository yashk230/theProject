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
    sname=models.CharField(max_length=30,verbose_name="Name of the Service")
    sdesc=models.CharField(max_length=150,verbose_name="Description of the Service")
    simage=models.ImageField(upload_to="service_image")
    sprice=models.IntegerField()
    
    def __str__(self):
        return self.sname
    
class Team(models.Model):
    name=models.CharField(max_length=50,verbose_name="Team Member Name")
    designation=models.CharField(max_length=50,verbose_name="Designation")
    image=models.ImageField(upload_to="team_member")
    
    def __str__(self):
        return self.name