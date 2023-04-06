import time
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.core.management import BaseCommand
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView, ListView, UpdateView, TemplateView

from mailing.forms import ClientForm, SignupForm, SigninForm

