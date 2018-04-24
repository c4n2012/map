from django.shortcuts import render
from .models import Workspace, Worker
from django.http import HttpResponse
import json

# Create your views here.
css_file_path = 'mapper/static/styles/dynamic'

def workspaces_list(request):
    workspaces = Workspace.objects.filter(stage__contains='2R').order_by('id')
    return render(request, 'mapper/workspaces_list.html', {'workspaces' : workspaces})

def css_maker(stage,workspaces_set):
    cssfile = open(css_file_path + stage + '.css', 'w')
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

def get_worker(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    sort_type = 1 # sort by surname
    workers = Worker.objects.filter(surname__contains=q).order_by('surname')
    if workers.count() == 0 :
        workers = Worker.objects.filter(login__contains=q).order_by('login')
        sort_type = 2 # sort by login  
    
    results = []
    for wkr in workers:
        workers_json = {}
        if sort_type == 1:
            workers_json = wkr.surname + " " + wkr.name + " " + wkr.login
        else: 
            workers_json = wkr.login + " " + wkr.surname + " " + wkr.name 
        results.append(workers_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)