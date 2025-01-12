from django.conf import settings
from django.http import FileResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import ProjectImage, Projects, Services, Team


# Create your views here.
def index(request):
    context={}
    context['projects']=Projects.objects.all()
    context['services']=Services.objects.all()
    context['team']=Team.objects.all()
    return render(request,'index.html',context)

def about(request):
    context={}
    context['team']=Team.objects.all()
    return render(request,'about.html',context)

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

def project_folder(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    file_path = project.pfile.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{project.pfile.name}"'
    return response

def service(request):
    context={}
    context['services']=Services.objects.all()
    return render(request,'service.html',context)

def service_info(request,sid):
    context={}
    context['services']=Services.objects.filter(id=int(sid))
    return render(request,'service-info.html',context)

def service_folder(request, service_id):
    service = get_object_or_404(Services, id=service_id)
    file_path = service.sfile.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{service.sfile.name}"'
    return response

def feature(request):
    return render(request,'feature.html')

def team(request):
    context={}
    context['team']=Team.objects.all()
    return render(request,'team.html',context)

def quote(request):
    return render(request,'quote.html')

def testimonial(request):
    return render(request,'testimonial.html')