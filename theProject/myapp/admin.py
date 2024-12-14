from django.contrib import admin

# Register your models here.
from .models import Projects, Services, Team


class ProjectAdmin(admin.ModelAdmin):
    list_display=['pname','pdesc','pimage','price']

admin.site.register(Projects,ProjectAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=['sname','sdesc','simage','sprice']
admin.site.register(Services,ServiceAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display=['name','designation','image']
admin.site.register(Team,TeamAdmin)