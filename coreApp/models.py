from django.db import models
from django.db.models.deletion import CASCADE

class Service(models.Model):
    title = models.CharField(max_length=255)
    package = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    quoteNeeded = models.BooleanField(default=0)
    timeFrame = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Info(models.Model):
    service = models.ForeignKey(Service, related_name='theService', on_delete=CASCADE)
    info = models.TextField()
    def __str__(self):
        return f"Info for {self.service.title}"

class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    published = models.DateField()
    lastUpdated = models.DateField()
    def __str__(self):
        return self.title