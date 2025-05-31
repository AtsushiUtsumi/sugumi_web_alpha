from django.urls import path
from . import views

urlpatterns = [
    path('login', views.show_login, name='login_get'),
    path('login/', views.login, name='login_post'),
    path('protected', views.protected, name='protected'),
]
