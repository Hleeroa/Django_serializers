from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)


class Measurements(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
