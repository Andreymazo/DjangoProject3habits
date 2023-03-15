from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):


    def handle(self, *args, **options):
        emails = ['test@testtest.ru', 'foreig_papa@papa.com']
        for i in emails:
            user = User.objects.create(
                email=i,
                is_superuser=False,
                is_staff=True
            )
            user.set_password('qwert123asd')
            user.save()
