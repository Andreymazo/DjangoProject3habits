from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='andreymazo@mail.ru',
            is_superuser=True,
            is_staff=True
        )
        user.set_password('qwert123asd')
        user.save()