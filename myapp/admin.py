from django.contrib import admin

# Register your models here.
from .models import ProjectImage, Projects, Services, ServicesImage, Team


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display=['pname','pdesc','price']
    inlines = [ProjectImageInline]
admin.site.register(Projects,ProjectAdmin)

class ServiceImageInline(admin.TabularInline):
    model =ServicesImage
    extra = 1
class ServiceAdmin(admin.ModelAdmin):
    list_display=['sname','sdesc','simage','sprice']
    inlines = [ServiceImageInline]
admin.site.register(Services,ServiceAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display=['name','designation','image']
admin.site.register(Team,TeamAdmin)