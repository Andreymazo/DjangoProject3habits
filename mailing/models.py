import django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User, CustomUserManager

NULLABLE = {'blank': True, 'null': True}



class Mailinglog(models.Model):
    mailing = models.CharField(max_length=100, verbose_name='Email')
    result = models.CharField(max_length=100, verbose_name='Result')
    last_attempt = models.DateTimeField(auto_now=True)


# class Emails(models.Model):#################ForeignKey  Client###########Hochu ostavit EmailField i FK
#     email = models.EmailField(max_length=50, verbose_name='Email')######

# Class StatusMssg(models.Model):
#     is_active = models.BooleanField(default=True)################ForeignKey  Mssg##############

# class Settings(models.Model):


    # status = models.CharField(max_length=10, choices=STATUSES, default=STATUS_CREATED)
    # time = models.TimeField()###Ne ponimau zachem time


