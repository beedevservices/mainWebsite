from django.db import models
from django.db.models.deletion import CASCADE

packageTypes = [
    ('Website Only', 'Creation or Updating of Website'),
    ('Add ons', 'Items that can be added on to any package'),
    ('Maintenance Packages', 'Plans for Website maintenance'),
    ('All inclusive', 'Starting from the ground up creating and maintaining website')
]

class Service(models.Model):
    title = models.CharField(max_length=255)
    package = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    quoteNeeded = models.BooleanField(default=0)
    packageType = models.CharField(max_length=255, choices=packageTypes, default='Website Only')
    order = models.IntegerField(default=1)
    timeFrame = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Info(models.Model):
    service = models.ForeignKey(Service, related_name='theService', on_delete=CASCADE)
    info = models.TextField()
    order = models.IntegerField(default=1)
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