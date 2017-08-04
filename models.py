from django.db import models
from django.utils import timezone

class Person(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
