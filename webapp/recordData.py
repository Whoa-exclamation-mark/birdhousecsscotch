__author__ = '162049'
import threading
import time
from helpers.logging import *
from webapp.temperatureStat import GetTemperature
from django.utils import timezone
from webapp.models import Temp


class Update(threading.Thread):
    def run(self):
        while True:
            t = Temp(time=timezone.now(), temperature=GetTemperature.temp)
            t.save()
            time.sleep(1000)


class Thread():
    t = Update()
    t.start()