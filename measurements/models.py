from django.db import models


class Sensor(models.Model):

    name = models.TextField()
    description = models.TextField()

class Measurement(models.Model):

    value = models.FloatField()
    sensors = models.ManyToManyField(Sensor, related_name='measurements')
    created_at = models.DateTimeField(
        auto_now_add=True
    )

