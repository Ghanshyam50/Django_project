from django.contrib import admin

# Register your models here.\ProjectModel
from .models import ClientModel, ProjectModel
    
    
admin.site.register(ClientModel)
admin.site.register(ProjectModel)
