from django.db import models


# Create your models here.
class Projects(models.Model):
    pname=models.CharField(max_length=50,verbose_name="Name of the Project")
    pdesc=models.TextField(verbose_name="Description of the Project")
    language=models.CharField(null=True,max_length=50,verbose_name="Language Used")
    framework=models.CharField(null=True,max_length=50,verbose_name="Framework Used")
    database=models.CharField(null=True,max_length=50,verbose_name="Database Used")
    userinterface=models.CharField(null=True,max_length=50,verbose_name="User Interface")
    webbrowser=models.CharField(null=True,max_length=50,verbose_name="Web Browser")
    ide=models.CharField(null=True,max_length=50,verbose_name="IDE Used")
    pimage=models.ImageField(null=True, blank=True,upload_to="project_images")
    pfile=models.FileField(null=True, blank=True,upload_to="project_files")
    ptype=models.CharField(null=True, blank=True,max_length=50,verbose_name="Project type")
    price=models.IntegerField()
    
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    
class Services(models.Model):
    sname=models.CharField(max_length=50,verbose_name="Name of the Service")
    sdesc=models.TextField(verbose_name="Description of the Service")
    simage=models.ImageField(upload_to="service_image")
    sfile=models.FileField(null=True, blank=True,upload_to="service_files")
    sprice=models.IntegerField()
    
    def __str__(self):
        return self.sname
    
class ServicesImage(models.Model):
    service = models.ForeignKey(Services, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_images/')

class Team(models.Model):
    name=models.CharField(max_length=50,verbose_name="Team Member Name")
    designation=models.CharField(max_length=50,verbose_name="Designation")
    image=models.ImageField(upload_to="team_member")
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    session_key = models.CharField(max_length=255)
    project=models.ForeignKey(Projects,on_delete=models.CASCADE,null=True,blank=True)
    services=models.ForeignKey(Services,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    total=models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Money(models.Model):
    project_id=models.ForeignKey(Projects,on_delete=models.CASCADE,verbose_name="Project ID",blank=True, null=True)
    service_id=models.ForeignKey(Services,on_delete=models.CASCADE,verbose_name="Project ID",blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)