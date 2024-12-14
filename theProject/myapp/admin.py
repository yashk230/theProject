from django.contrib import admin

# Register your models here.
from .models import Projects, Services


class ProjectAdmin(admin.ModelAdmin):
    list_display=['pname','pdesc','pimage','price']

admin.site.register(Projects,ProjectAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=['sname','sdesc','simage','sprice']
admin.site.register(Services,ServiceAdmin)