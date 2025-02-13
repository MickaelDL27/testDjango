from django.conf import settings
from django.db import models
from django.utils import timezone

class Voetbalspelers(models.Model):
    naam = models.CharField(max_length=255)
    actuele_club = models.CharField(max_length=255)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datum_invoer = models.DateTimeField(auto_now_add=True)
    datum_laatste_aanpassing = models.DateTimeField(auto_now=True)

    def publish(self):
        self.datum_invoer = timezone.now()
        self.save()

    def __str__(self):
        return self.naam