# Generated by Django 4.1.6 on 2023-03-22 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
    ]