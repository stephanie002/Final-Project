from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)

class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.Charfield(max_length=80)
    custom_message = models.CharField(max_length=80)
    self.published_date = timezone.now()
    self.save()

    def __str__(self):
        return self.title
# Create your models here.
