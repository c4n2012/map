from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Workspace

# admin.site.register(Workspace)

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    pass