from buschecker.models import ScheduledStopTimes, BusStop
from datetime import datetime


def getPossibleStops(directionChoice: str, areaChoice: str):

    stops = BusStop.objects.filter(scheduledstoptimes__direction=directionChoice, area__icontains=areaChoice).distinct()
    return stops



