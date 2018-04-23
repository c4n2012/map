from django.shortcuts import render
from .models import Workspace

# Create your views here.

def workspaces_list(request):
    workspaces = Workspace.objects.filter(stage__contains='2R').order_by('id')
    return render(request, 'mapper/workspaces_list.html', {'workspaces' : workspaces})

def css_maker(stage,workspaces_set):
    cssfile = open('mapper/static/styles/dynamic'+stage+'.css', 'w')
    for workspace in workspaces_set:
        raw = ".workspace-position-" 
        raw += workspace.stage + str(workspace.id)
        raw += " { transform: translate("
        raw += str(workspace.xPos)
        raw += "px, "
        raw += str(workspace.yPos)
        raw += "px) scale(1,1);background-position: 0px 0px;} "
        cssfile.write(raw + '\n')
        raw = ".workspace-position-"
        raw += workspace.stage + str(workspace.id)
        raw += ":hover{ transform: translate("
        raw += str(workspace.xPos)
        raw += "px, "
        raw += str(workspace.yPos-5)
        raw +="px) scale(1.1,1.2); opacity: 1;}"
        cssfile.write(raw + '\n')
    cssfile.close()
     


def map2R(request):
    stage='2R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})

def map2R_admin(request):
    stage='2R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map_admin.html', {'workspaces_set' : workspaces_set})

def map2L(request):
    stage='2L'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})
