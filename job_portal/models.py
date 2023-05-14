from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **kwargs)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


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
