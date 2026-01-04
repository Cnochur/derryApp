from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from buschecker.services import getPossibleStops
from .models import ScheduledStopTimes, BusStop
from datetime import datetime

# Create your views here.

def home(request):
    if request.method == 'POST':
        try:
            directionChoice: str = request.POST['directionChoice']
            areaChoice: str = request.POST['areaChoice'].title()
            stops = getPossibleStops(directionChoice, areaChoice)
        except Exception:
            stops = []

        return render(request, template_name='buschecker/index.html', context={'stops': stops})
    return render(request, template_name='buschecker/index.html')

def bus_times(request):
    stop_id = request.GET['stop_id']

    if not stop_id:
        return JsonResponse({'error': 'stop_id is required'}, status=400)

    try:
        stop = BusStop.objects.get(id=stop_id)
    except BusStop.DoesNotExist:
        return JsonResponse({'error': 'stop_id does not exist'}, status=400)

    currentTime = datetime.now().time()

    all_times = ScheduledStopTimes.objects.filter(stop=stop).order_by('arrival_time')
    times_list = [
        {"service": t.route.service_number, "time": t.arrival_time.strftime("%H:%M")}
        for t in all_times if t.arrival_time >= currentTime
    ][:4]
    print(times_list)
    return JsonResponse(times_list, safe=False)
