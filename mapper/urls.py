from django.urls import path
from . import views

urlpatterns = [
    path('',views.map2R),
    path('map1R',views.map1R, name='map1R'),
    path('map2R',views.map2R, name='map2R'),
    path('map3R',views.map3R, name='map3R'),
    path('map4R',views.map4R, name='map4R'),

    path('map1L',views.map1L, name='map1L'),
    path('map2L',views.map2L, name='map2L'),
    path('map3L',views.map3L, name='map3L'),
    path('map4L',views.map4L, name='map4L'),

    path('map1R_admin', views.map1R_admin, name='map1R_admin'),
    path('map2R_admin', views.map2R_admin, name='map2R_admin'),
    path('map3R_admin', views.map3R_admin, name='map3R_admin'),
    path('map4R_admin', views.map4R_admin, name='map4R_admin'),

    path('map1L_admin', views.map1L_admin, name='map1L_admin'),
    path('map2L_admin', views.map2L_admin, name='map2L_admin'),
    path('map3L_admin', views.map3L_admin, name='map3L_admin'),
    path('map4L_admin', views.map4L_admin, name='map4L_admin'),

    # path('list/', views.workspaces_list, name='workspaces_list'),
    path('api/get_worker/', views.get_worker, name='get_worker'),
    path('api/get_worker_position/', views.get_worker_position, name='get_worker_position'),
]