from django.db import models

# Create your models here.


class Candidates (models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True)
    mobile_numb = models.CharField(max_length=200, null=True)
    dob = models.IntegerField(max_length=150, null=True)





