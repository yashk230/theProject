from django.contrib import admin

# Register your models here.
from .models import Projects


class ProjectAdmin(admin.ModelAdmin):
    list_display=['pname','pdesc','pimage','price']

admin.site.register(Projects,ProjectAdmin)