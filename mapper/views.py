from django.shortcuts import render, redirect
from .models import Workspace, Worker
from django.http import HttpResponse, HttpResponseRedirect
import json, re
from django.urls import reverse

# Create your views here.
css_file_path = 'mapper/static/styles/dynamic'
#for pythonanywere
## css_file_path = 'map/mapper/static/styles/dynamic'

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

def map1R(request):
    stage='1R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})
def map2R(request):
    stage='2R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})
def map3R(request):
    stage='3R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})
def map4R(request):
    stage='4R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})

def map1L(request):
    stage='1L'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})
def map2L(request):
    stage='2L'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})
def map3L(request):
    stage='3L'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})
def map4L(request):
    stage='4L'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})

def map1R_admin(request):
    stage='1R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map_admin.html', {'workspaces_set' : workspaces_set})
def map2R_admin(request):
    stage='2R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map_admin.html', {'workspaces_set' : workspaces_set})
def map3R_admin(request):
    stage='3R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map_admin.html', {'workspaces_set' : workspaces_set})
def map4R_admin(request):
    stage='4R'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map_admin.html', {'workspaces_set' : workspaces_set})

def map1L_admin(request):
    stage='1L'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map_admin.html', {'workspaces_set' : workspaces_set})
def map2L_admin(request):
    stage='2L'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map_admin.html', {'workspaces_set' : workspaces_set})
def map3L_admin(request):
    stage='3L'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map_admin.html', {'workspaces_set' : workspaces_set})
def map4L_admin(request):
    stage='4L'
    workspaces_set = Workspace.objects.filter(stage__contains=stage).order_by('-xPos').order_by('yPos')
    css_maker(stage,workspaces_set)
    return render(request, 'mapper/map_admin.html', {'workspaces_set' : workspaces_set})

def get_worker(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        sort_type = 1 # sort by surname
        workers = Worker.objects.filter(surname__contains=q.capitalize()).order_by('surname')[:20]
    if workers.count() == 0 :
        workers = Worker.objects.filter(login__contains=q).order_by('login')[:20]
        sort_type = 2 # sort by login  
    
    results = []
    for wkr in workers:
        workers_json = {}
        if sort_type == 1:
            workers_json = wkr.surname + " " + wkr.name + " - " + wkr.login
        else: 
            workers_json = wkr.surname + " " + wkr.name + " - " + wkr.login
            # workers_json = wkr.login + " - " + wkr.surname + " " + wkr.name 
        results.append(workers_json)
    data = json.dumps(results)
    # if data.count() == 0:
    #     data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def get_worker_position(request):
    if request.method == "GET":
        worker_login_req = request.GET.get('login', '').split(" - ") # получаем список из реквеста чтоб использовать логин для запроса в БД
        reg = re.compile('[^a-z.]') # разрешенные символы
        # print (reg.sub('',q[1]))
        worker_login_req = reg.sub('',worker_login_req[1]) # удаление из  логина плохих символов
        workspaces_set = Workspace.objects.filter(login__contains=worker_login_req).order_by('-xPos').order_by('yPos')
    data = workspaces_set[0].stage + " " + str(workspaces_set[0].xPos) + " " + str(workspaces_set[0].yPos)
    mimetype = 'application/json'
    # return HttpResponse(data, mimetype)
    stage = workspaces_set[0].stage
    redir_map = "map"+workspaces_set[0].stage
    # redir_map = "/" + "map"+workspaces_set[0].stage
    print ("redirection stage = " + redir_map)
    # css_maker(stage,workspaces_set)
    # return HttpResponseRedirect('/'+ redir_map)
    return render(request, 'mapper/map.html', {'workspaces_set' : workspaces_set})

