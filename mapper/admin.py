from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Workspace, Worker

class WorkspaceAdmin(admin.ModelAdmin):
   list_display = ('workspaceNum','phone','login','ip','stage','id')
   # pass

# @admin.register(Workspace, WorkspaceAdmin)
admin.site.register(Workspace, WorkspaceAdmin)

class WorkerAdmin(admin.ModelAdmin):
	 list_display = ('login','surname')
admin.site.register(Worker, WorkerAdmin)