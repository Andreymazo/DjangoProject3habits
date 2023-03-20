# Generated by Django 4.1.6 on 2023-03-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_habit_options_alter_habit_place_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={},
        ),
        migrations.AlterField(
            model_name='habit',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time_fulfil',
            field=models.IntegerField(verbose_name='время, которое предположительно потратит пользователь на выполнение привычки'),
        ),
    ]
