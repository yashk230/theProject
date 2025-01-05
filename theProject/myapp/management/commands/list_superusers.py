# File: myapp/management/commands/list_superusers.py
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Lists all superusers with their usernames and email addresses'

    def handle(self, *args, **kwargs):
        superusers = User.objects.filter(is_superuser=True)
        for user in superusers:
            self.stdout.write(self.style.SUCCESS(f'Username: {user.username}, Email: {user.email}'))

# command to run the code
# python manage.py list_superusers