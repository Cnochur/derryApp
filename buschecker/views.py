from django.http import JsonResponse
from django.shortcuts import render
from buschecker.services import getPossibleStops
# from .models import
# Create your views here.

def home(request):
    if request.method == 'POST':
        directionChoice: str = request.POST['directionChoice']
        areaChoice: str = request.POST['areaChoice'].title()
        stops = getPossibleStops(directionChoice, areaChoice)

        return render(request, template_name='buschecker/index.html', context={'stops': stops})
    return render(request, template_name='buschecker/index.html')


def stops(request):
    area = request.GET['areaChoice']
    direction = request.GET['directionChoice']
    areaStops = getPossibleStops(direction, area)

    stopsList = []

    for stop in areaStops:
        stopsList.append(
            {"id": stop.id, "name": stop.name, "latitude": stop.latitude, "longitude": stop.longitude}
        )

    return JsonResponse(stopsList, safe=False)