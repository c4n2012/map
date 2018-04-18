from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_dynamic_map),
    path('map2R',views.map2R),
    path('map2R_admin', views.map2R_admin),
    path('list/', views.workspaces_list),

    path('test/', views.test, name=''),
]