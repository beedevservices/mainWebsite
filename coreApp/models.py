from django.db import models
from django.db.models.deletion import CASCADE

packageTypes = [
    ('Websites', 'Create or Update websites'),
    ('Tutoring', 'Tutoring Services'),
    ('Career', 'Resume and other Career Services'),
    ('Maintenance', 'Packages for routing website upkeep'),
    ('Add Ons', 'Items that can be added on to any package'),
    ('All Inclusive', 'Starting from the ground up creating and maintaining website'),
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