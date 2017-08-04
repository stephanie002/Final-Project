from django.db import models
from django.contrib.auth.models import User


class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    custom_message = models.CharField(max_length=80)
    user = models.ForeignKey(User, null=True, related_name='profile')


    def __str__(self):
        return self.first_name

    def create(self):
        self.save()
