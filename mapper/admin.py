from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Workspace,Worker

# admin.site.register(Workspace)

@admin.register(Workspace)
@admin.register(Worker)
class WorkspaceAdmin(admin.ModelAdmin):
    pass