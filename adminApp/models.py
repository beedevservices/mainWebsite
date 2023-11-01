from django.db import models
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE
from coreApp.keys import *

class ManagerManager(models.Manager):
    def validate(self, form):
        errors = {}
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email already in use'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors

class Manager(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = ManagerManager()

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def register(self):
        self.save()

    def __str__(self):
        return self.firstName
    def fullName(self):
        return f'{self.firstName} {self.lastName}'
    
class ManagerProfile(models.Model):
    manager = models.OneToOneField(Manager, unique=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.manager.firstName} Profile'

# class Department(models.Model):
#     pass

# class ManagerJobs(models.Model):
#     pass

# class ManagerEmployees(models.Model):
#     pass