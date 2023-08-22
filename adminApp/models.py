from django.db import models
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE
from coreApp.keys import *

class EmployeeManager(models.Manager):
    pass
