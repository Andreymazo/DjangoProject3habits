import datetime
import threading
import time

import pytz
from django import forms
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm
from rest_framework.exceptions import ValidationError

from config import settings

NULLABLE = {'blank': True, 'null': True}

class CustomUserManager(UserManager):

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    # use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects = CustomUserManager()


    username = None
    email = models.EmailField(
        verbose_name="Почта",
        max_length=54,
        unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватарка', blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
class Habit(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=150, verbose_name='место', default='Nowhere')
    time_todo = models.TimeField(auto_now_add=True, verbose_name='время, когда необходимо выполнять привычку')##Изменяется при изменении модели
    action = models.CharField(max_length=150, verbose_name='действие, которое представляет из себя привычка')
    useful = models.BooleanField(**NULLABLE, verbose_name='полезная привычка или нет', default=True)

    if_pleasant = models.ForeignKey('users.Habit', **NULLABLE, on_delete=models.CASCADE, related_name='canbewith_useful', verbose_name='привычка, которую можно привязать к выполнению полезной привычки')

    # def filter_clients(self, instance): Nikak ne vvesti globalnoe ogranichenie
    #     query_set = Habit.objects.all().filter(id=self.client_id)
    #     print("------------------------", instance)
    #     return query_set
    if_connected = models.ForeignKey('self', **NULLABLE, on_delete=models.CASCADE, related_name='mustbewith_useful', verbose_name='привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных')

    period = models.CharField(max_length=100, verbose_name='периодичность выполнения привычки для напоминания в днях', **NULLABLE)
    prize = models.CharField(max_length=150, verbose_name='чем пользователь должен себя вознаградить после выполнения', **NULLABLE)

    time_fulfil = models.IntegerField(verbose_name='время, которое предположительно потратит пользователь на выполнение привычки', **NULLABLE)
    is_published = models.BooleanField(**NULLABLE, verbose_name='привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки', default=False)
    updated_at = models.DateTimeField(auto_now=True)
    time_to_doo_habit = models.TimeField(**NULLABLE, verbose_name='время, когда необходимо выполнять привычку')##Изменяется при изменении модели
    def __str__(self):
        return f'{self.action} {self.time_to_doo_habit}'# related to: {self.client}'
    # class Meta:users_user_groups
    #     permissions = [
    #         ("set_is_published", "Can publish habit"),
    #         # ("add_habit", "Can add habit"),
    #         # ("delete_habit", "Can delete habit"),
    #     ]
    # class Meta:
    #
    #     fields = ('action', 'if_connected', 'prize', 'place', 'period')
    #     # field = '__all__'
# class HabitForm(ModelForm):
#     model = Habit
#     fields = '__all__'

    def clean(self):### Ne mogut odnovremenno bit i prize i if_connected
        from django.core.exceptions import ValidationError
        if self.prize and self.if_connected:
            raise ValidationError('AYAYAYAYAY')
        return self.prize
    def safe(self, *args, **kwargs):##Proveryaem na izmenenie polya

        while True:
            time.sleep(25)##Kazhdie 25v sec proveryaet pole time_to_doo_habit
            # thread = threading.Thread(  # создание отдельного потока
            #     target=print, args=("данные сайта обновились",))
            # thread.start()
            now = time.time()
            delta = abs(self.time_to_doo_habit.second - now)
            print('now-----------',now)
            if delta < 30:
            # if self.pk is not None:
            #     now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
                print('delta', delta)
            print('_______________________')
                # if (now - self.updated_at).seconds > 4*60*60:
                #     send_notify_update.delay(self/pk)
            super().save(*args, **kwargs)

#############################################################
    # def clean(self):
    #     clean_data = super(Habit, self).clean()#HabitForm, self
    #     if_connected = clean_data['if_connected']
    #     prize = clean_data['prize']
    #     if if_connected and prize:
    #         raise ValidationError("You may not choose both fields!")
    #
    #     return clean_data
##############################################################
    # def clean_if_connected(self):
    #     # clean_data = super(Habit, self).clean()#HabitForm, self
    #     if_connected = self.clean_if_connected['if_connected']
    #     prize = self.clean_if_connected['prize']
    #     if if_connected and prize:
    #         raise ValidationError("You may not choose both fields!")
    #
    #     return self.clean_if_connected
        #
        # if_connected = self.clean_if_connected['if_connected']
        # prize = self.clean_if_connected['prize']
        # if if_connected and prize:
        #     raise ValidationError
        # return if_connected
# class HabitForm(ModelForm):
#     class Meta:
#         model = Habit
#         fields = ['action', 'if_connected', 'prize', 'place', 'period']
                 #'__all__'

    def clean_if_connected(self):
        if_connected=self.clean_if_connected['if_connected']
        prize = self.clean_if_connected['prize']
        if if_connected and prize:
            raise ValidationError
        return if_connected
    # def clean_prize(self):
    #     if_connected = self.clean_prize['if_connected']
    #     prize = self.clean_prize['prize']
    #     if if_connected and prize:
    #         raise ValidationError
    #     return prize
# class IntroductionForm(ModelForm):
#     class Meta:
#          ...
# def clean_fieldA(self):
#     fieldA = self.cleaned_data['fieldA']
#     fieldB = self.cleaned_data['fieldB']
#     if self.instance.fieldB == fieldB and  self.instance.fieldB == fieldA:
#             raise ValidationError("You may not choose both fields")

    # return fieldA

