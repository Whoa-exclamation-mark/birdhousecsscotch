__author__ = '162049'
import threading
import time
from webapp.temperatureStat import GetTemperature
from webapp.motionDetector import GetMotion
from django.utils import timezone
from webapp.models import *


class Update(threading.Thread):
    def run(self):
        while True:
            t = Temp(time=timezone.now(), temperature=GetTemperature.temp)
            t.save()
            m = Motion(time=timezone.now(), motion=GetMotion.motion)
            m.save()
            time.sleep(1000)


class Thread():
    t = Update()
    t.start()