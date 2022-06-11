from django.db import models
# from .misc import *
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE
from django.shortcuts import reverse
from django_countries.fields import CountryField

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already taken'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    level = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

class Profile(models.Model):
    img = models.ImageField(upload_to='profileImgs', default='bee.png')
    user = models.OneToOneField(User, unique=True, on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user.firstName} {self.user.lastName} Profile'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='companyLogos', default='bee.png')
    user = models.ForeignKey(User, related_name='companyUser', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def fullCompany(self):
        return f'{self.user.firstName} from {self.name}'
    def __str__(self):
        return self.name

class Position(models.Model):
    role = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='positionUser', on_delete=CASCADE)
    company = models.ForeignKey(Company, related_name='positionCompany', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def companyRoll(self):
        return f'{self.user.firstName}, {self.role} from {self.company.name}'
    def __str__(self):
        return self.role

class StatusType(models.Model):
    statusType = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.statusType

class Status(models.Model):
    status = models.CharField(max_length=255)
    typeStatus = models.ForeignKey(StatusType, related_name='theType' , on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.status

CATEGORY = {
    ('ADD', 'Add On'),
    ('ONE', 'One Time'),
    ('REC', 'Recurring')
}

class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY, max_length=3)
    description = models.TextField()
    turnaround = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
