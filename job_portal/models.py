from django.db import models
from django.utils import timezone


# Create your models here.


class Candidates (models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True)
    mobile_numb = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now)






