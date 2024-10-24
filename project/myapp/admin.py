from django.contrib import admin

# Register your models here.
from .models import Projects


class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','ptype','pname','pimage']
    
admin.site.register(Projects,ProjectAdmin)
