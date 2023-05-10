from django.db import models
from django.utils import timezone


# Create your models here.

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class Job(models.Model):
    job_name = models.CharField(max_length=200, null=True),
    position = models.CharField(max_length=100, null=True),
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    location = models.CharField(max_length=100, null=False),
    salary = models.IntegerField(null=True),
    experience = models.IntegerField(null=True),
    description = models.CharField(max_length=255, null=True)


class Candidates (models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True)
    mobile_numb = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now)






