from  . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('times/', views.bus_times, name='bus_times'),

]