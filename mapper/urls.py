from django.urls import path
from . import views

urlpatterns = [
    path('',views.map2R),
    path('map2R',views.map2R, name='map2R'),
    path('map2R_admin', views.map2R_admin, name='map2R_admin'),
    path('list/', views.workspaces_list, name='workspaces_list'),
    path('api/get_worker/', views.get_worker, name='get_worker'),
]