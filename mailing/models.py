from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Client(models.Model):

    email = models.CharField(unique=True, max_length=100, verbose_name='Почта')
    name = models.CharField(max_length=200, verbose_name='Фамилия Имя Отчество')
    comment = models.TextField(max_length=300, **NULLABLE)
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name}'

class Mssg(models.Model):

    STATUS_DONE = 'done'
    # STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'

    STATUSES = (
        (STATUS_DONE, False),
        # (STATUS_CREATED, 'создано'),
        (STATUS_STARTED, True),
    )
    PERIOD_DAY = 86400
    PERIOD_WEEK = 604800
    PERIOD_MONTH = 2419200
    PERIODS = (
        (PERIOD_DAY, 'день=86400'),
        (PERIOD_WEEK, 'неделя=604800'),
        (PERIOD_MONTH, 'месяц=2419200'),
    )

    link = models.ForeignKey('mailing.Client', max_length=100, verbose_name='Какому клиенту относится', on_delete=models.CASCADE)
    text = models.CharField(max_length=100, verbose_name='Текст сообщения')
    ###auto_now  - update from save()##########ForeignKey Mssg
    status = models.BooleanField(default=False)
    period = models.TimeField(auto_now=True, max_length=10, choices=PERIODS)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.text}'
# class MssgManager(models.Manager):

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
class Emails(models.Model):
    comment = models.ForeignKey('mailing.Client', max_length=100, verbose_name='Какому клиенту относится', on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, verbose_name='Емэйл')
    status_complete = models.BooleanField(default=False)##Client zapolniaet emails poka ne postavit staetus_complete

    class Meta:
        verbose_name = "Емэйл"
        verbose_name_plural = 'Емэйлы'
    def __str__(self):
        return f'{self.email} '

