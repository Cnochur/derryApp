from buschecker.models import ScheduledStopTimes, BusStop
from datetime import datetime


def getPossibleStops(directionChoice: str, areaChoice: str):

    times = ScheduledStopTimes.objects.filter(direction=directionChoice)
    stops = BusStop.objects.filter(scheduledstoptimes__in=times, area=areaChoice)

    return stops



