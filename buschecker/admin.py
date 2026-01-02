from django.contrib import admin

from buschecker.models import BusStop, Route, ScheduledStopTimes


admin.site.register(BusStop)
admin.site.register(Route)
admin.site.register(ScheduledStopTimes)
