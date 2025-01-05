from django.conf import settings
from django.shortcuts import redirect, render

from .models import ProjectImage, Projects, Services, Team


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
    context={}
    context['projects']=Projects.objects.all()
    return render(request,'project.html',context)

def project_info(request,pid):
    context={}
    context['projects']=Projects.objects.filter(id=int(pid))
    context['project_images']=ProjectImage.objects.filter(project=int(pid))
    return render(request,'project-info.html',context)

def service(request):
    context={}
    context['services']=Services.objects.all()
    return render(request,'service.html',context)

def service_info(request,sid):
    context={}
    context['services']=Services.objects.filter(id=int(sid))
    return render(request,'service-info.html',context)

def feature(request):
    return render(request,'feature.html')

def team(request):
    return render(request,'team.html')

def quote(request):
    return render(request,'quote.html')

def testimonial(request):
    return render(request,'testimonial.html')