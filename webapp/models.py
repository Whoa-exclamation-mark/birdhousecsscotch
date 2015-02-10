from django.db import models

# Create your models here.


class Temp(models.Model):
    time = models.DateTimeField('Time')
    temperature = models.IntegerField(max_length=2, default=0)


class Motion(models.Model):
    time = models.DateTimeField('Time')
    motion = models.BooleanField(default=True)
