from django.shortcuts import render

from .models import Projects


# Create your views here.
def index(request):
    projects=Projects.objects.all()
    context={}
    context["projects"]=projects
    return render (request,'index.html',context)

def about (request):
    return render (request,'about.html')

def  contact(request):
    return render (request,'contact.html')

def feature (request):
    return render (request,'feature.html')

def project (request):
    return render (request,'project.html')

def quote (request):
    return render (request,'quote.html')

def service (request):
    return render (request,'service.html')

def team (request):
    return render (request,'team.html')

def testimonial (request):
    return render (request,'testimonial.html')