from  . import views
from django.urls import path, include

app_name = 'walls'
urlpatterns = [
    path('', views.home, name='home'),
]