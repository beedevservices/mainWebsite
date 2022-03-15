from django.db import models
from .misc import *
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE

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
    permissions = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
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
