from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_dynamic_map, name='show_dynamic_map'),
    path('list/', views.workspaces_list, name='workplaces_list'),
    path('test/', views.test, name=''),
]