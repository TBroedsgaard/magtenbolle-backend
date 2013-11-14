from django.db import models
from tastypie.models import create_api_key
from django.contrib.auth.models import User

# Hook create_api_key to user post-create signal
models.signals.post_save.connect(create_api_key, sender=User)


class ContactPerson(models.Model):
    FirstName = models.CharField(max_length=200)
    SurName = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    PhoneNumber = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)
    Age = models.IntegerField()
    Weight = models.IntegerField()

    def __unicode__(self):
        return "{0.id}: {0.FirstName} {0.SurName}".format(self)


class Customer(models.Model):
    FirstName = models.CharField(max_length=200)
    SurName = models.CharField(max_length=200)
    Age = models.IntegerField()
    Weight = models.IntegerField()

    def __unicode__(self):
        return "{0.id}: {0.FirstName} {0.SurName}".format(self)


class Bike(models.Model):
    Size = models.CharField(max_length=20)
    Type = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "{0.id}: {0.Type} {0.Size} {0.Price}".format(self)


class Payment(models.Model):
    Amount = models.DecimalField(max_digits=8, decimal_places=2)
    Type = models.CharField(max_length=50)
    Accepted = models.BooleanField()

    def __unicode__(self):
        return "{0.id}: {0.Amount} {0.Type} {0.Accepted}".format(self)


class Checkin(models.Model):
    DateTime = models.DateTimeField()
    ContactPerson = models.ForeignKey(ContactPerson)
    Customers = models.ManyToManyField(Customer, blank=True)
    Bikes = models.ManyToManyField(Bike, blank=True)
    Payment = models.OneToOneField(Payment)

    def __unicode__(self):
        return "{0.id}: {0.DateTime} {0.ContactPerson}".format(self)
