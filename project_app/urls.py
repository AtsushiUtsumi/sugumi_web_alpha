from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='home'),
    path('home/<str:name>/', views.hello, name='hello'),
    path('project-list', views.project_list, name='project_list'),
    path('project-detail/<int:project_id>', views.project_detail, name='project_detail'),
]
