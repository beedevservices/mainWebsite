from django.db import models
from django.db.models.deletion import CASCADE

class Service(models.Model):
    title = models.CharField(max_length=255)
    package = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    quoteNeeded = models.BooleanField(default=0)
    timeFrame = models.CharField(max_length=255)

class Info(models.Model):
    service = models.ForeignKey(Service, related_name='theService', on_delete=CASCADE)
    info = models.TextField()


