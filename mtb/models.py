from django.db import models
from tastypie.models import create_api_key
from django.contrib.auth.models import User

# Hook create_api_key to user post-create signal
models.signals.post_save.connect(create_api_key, sender=User)


class Customer(models.Model):
    FirstName = models.CharField(max_length=200)
    SurName = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    PhoneNumber = models.CharField(max_length=20)
    Street = models.CharField(max_length=200)
    StreetNumber = models.CharField(max_length=10)
    Age = models.IntegerField()
    Weight = models.IntegerField()

    def __unicode__(self):
        return "{0.id}: {0.FirstName} {0.SurName}".format(self)


class Participant(models.Model):
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


class Registration(models.Model):
    DateTime = models.DateTimeField()
    Customer = models.ForeignKey(Customer)
    Participants = models.ManyToManyField(Participant, blank=True)
    Bikes = models.ManyToManyField(Bike, blank=True)

    def __unicode__(self):
        return "{0.id}: {0.DateTime} {0.Customer}".format(self)
