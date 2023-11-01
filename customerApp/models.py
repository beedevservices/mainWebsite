from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save

class CustomerManager(models.Manager):
    def validate(self, form):
        errors = {}
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email already in use'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors
    
class Customer(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)

    objects = CustomerManager()

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def register(self):
        self.save()

    def __str__(self):
        return self.firstName
    def fullName(self):
        return f'{self.firstName} {self.lastName}'
    
class CustomerProfile(models.Model):
    customer = models.OneToOneField(Customer, unique=True, on_delete=models.CASCADE)
    address01 = models.CharField(max_length=255, blank=True)
    address02 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    busType = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f'{self.customer.firstName} Profile'
    def address(self):
        return f'{self.address01} {self.address02} {self.city} {self.state} {self.zip}'
    def tel(self):
        return self.phone

def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(customer=instance)
        post_save.connect(create_customer_profile, sender=Customer)
