from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Counts the number of superusers'

    def handle(self, *args, **kwargs):
        superusers = User.objects.filter(is_superuser=True)
        superuser_count = superusers.count()
        self.stdout.write(self.style.SUCCESS(f'Total number of superusers: {superuser_count}'))

# command to run the code
# python manage.py count_superusers