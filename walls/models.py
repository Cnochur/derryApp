from django.db import models

# Create your models here.
class Stop(models.Model):
    tourPosition = models.PositiveIntegerField(null=False)
    name = models.CharField(null=False)
    description = models.TextField(null=False)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f"{self.tourPosition} - {self.name}"

    class Meta:
        ordering = ['tourPosition']
