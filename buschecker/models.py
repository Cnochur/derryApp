from django.db import models

from walls.models import Stop


# Create your models here.
class BusStop(models.Model):
    name = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.area})"

class Route(models.Model):
    service_number = models.CharField(max_length=5)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.service_number}"

class ScheduledStopTimes(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(BusStop, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    direction = models.CharField(max_length=10, choices=[('to_city', 'To City'), ('from_city', 'From City')])

    class Meta:
        ordering = ['arrival_time']

    def __str__(self):
        return f'{self.route.service_number} at {self.stop} - {self.arrival_time}'