from django.db import models
from tastypie.models import create_api_key
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


# Hook create_api_key to user post-create signal
models.signals.post_save.connect(create_api_key, sender=User)
