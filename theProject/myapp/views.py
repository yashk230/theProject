from django.conf import settings
from django.shortcuts import redirect, render

from .models import Projects, Services, Team


# Create your views here.
def index(request):
    context={}
    context['projects']=Projects.objects.all()
    context['services']=Services.objects.all()
    context['team']=Team.objects.all()
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')

def service(request):
    return render(request,'service.html')

def feature(request):
    return render(request,'feature.html')

def team(request):
    return render(request,'team.html')

def quote(request):
    return render(request,'quote.html')

def testimonial(request):
    return render(request,'testimonial.html')