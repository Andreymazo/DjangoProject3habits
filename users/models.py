from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
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
    place = models.CharField(max_length=150, verbose_name='место', **NULLABLE)
    time_todo = models.TimeField(auto_now_add=True, verbose_name='время, когда необходимо выполнять привычку')##Изменяется при изменении модели
    action = models.CharField(max_length=150, verbose_name='действие, которое представляет из себя привычка')
    useful = models.BooleanField(**NULLABLE, verbose_name='полезная привычка или нет', default=True)
    if_pleasant = models.ForeignKey('self', **NULLABLE, on_delete=models.CASCADE, related_name='canbewith_useful', verbose_name='привычка, которую можно привязать к выполнению полезной привычки')
    if_connected = models.ForeignKey('self', **NULLABLE, on_delete=models.CASCADE, related_name='mustbewith_useful', verbose_name='привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных')
    period = models.CharField(max_length=100, verbose_name='периодичность выполнения привычки для напоминания в днях')
    prize = models.CharField(max_length=150, verbose_name='чем пользователь должен себя вознаградить после выполнения')
    time_fulfil = models.IntegerField(max_length=10, verbose_name='время, которое предположительно потратит пользователь на выполнение привычки')
    is_published = models.BooleanField(**NULLABLE, verbose_name='привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки', default=False)

    class Meta:
        permissions = [
            ("set_is_published", "Can publish habit"),
            # ("add_habit", "Can add habit"),
            # ("delete_habit", "Can delete habit"),
        ]



