from django.shortcuts import render
from .models import Stop
# Create your views here.

def home(request):
    stops = Stop.objects.all()
    return render(request, template_name='walls/index.html', context={'stops': stops})