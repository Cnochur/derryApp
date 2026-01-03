from django.shortcuts import render
from buschecker.services import getPossibleStops
# from .models import
# Create your views here.

def home(request):
    if request.method == 'POST':
        directionChoice: str = request.POST['directionChoice']
        areaChoice: str = request.POST['areaChoice'].title()

        stops = getPossibleStops(directionChoice, areaChoice)

        print(stops)
    return render(request, template_name='buschecker/index.html')