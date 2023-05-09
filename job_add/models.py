from django.db import models

# Create your models here.
JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class Job(models.Model):
    job_name = models.CharField(max_length=200,null=True),
    position = models.CharField(max_length = 100, null = True),
    job_type = models.CharField(choices = JOB_TYPE, max_length = 1)
    location = models.CharField(max_length=100, null=False),
    salary = models.IntegerFiled(null=true),
    experience = models.IntegerFiled(null=True),
    description = models.CharField(max_length = 255, null = True)

    def __str__(self):
        return  self.job_name




