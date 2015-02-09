__author__ = '162049'
from django.utils import timezone


class Logging():
    def info(str):
        print("[", timezone.now(), "]", str)