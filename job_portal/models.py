from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    job_name = models.CharField(max_length=200, default='')
    position = models.CharField(max_length=100, default='')
    JOB_TYPE = (
        ('1', "Full time"),
        ('2', "Part time"),
        ('3', "Internship"),
    )
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    location = models.CharField(max_length=100, default='')
    salary = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)
    description = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.job_name

class UserJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

class Candidates(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True)
    mobile_numb = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/')
    name = models.CharField(max_length=255)
    about_me = models.TextField()
    my_skills = models.TextField()
    my_experience = models.TextField()

    def __str__(self):
        return self.name