from django.db import models
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE
from coreApp.keys import *

class EmployeeManager(models.Manager):
    def validate(self, form):
        errors = {}
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email already in use'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors

class Employee(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = EmployeeManager()

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def register(self):
        self.save()

    def __str__(self):
        return self.firstName
    def fullName(self):
        return f'{self.firstName} {self.lastName}'
    
class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee, unique=True, on_delete=models.CASCADE)
    address01 = models.CharField(max_length=255, blank=True)
    address02 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    hireDate = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True)
    promotionDate = models.DateField(blank=True, null=True)
    terminated = models.BooleanField(default=0)
    terminationDate = models.DateField(blank=True, null=True)
    def __str__(self):
        return f'{self.employee.firstName} Profile'
    def address(self):
        return f'{self.address01} {self.address02} {self.city} {self.state} {self.zip}'
    def tel(self):
        return self.phone
    

# class EmployeeJobs(models.Model):
#     pass