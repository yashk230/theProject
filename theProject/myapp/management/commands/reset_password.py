# File: myapp/management/commands/reset_password.py
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Resets the password for a given user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username of the user')
        parser.add_argument('new_password', type=str, help='The new password for the user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        new_password = kwargs['new_password']

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Password for user {username} has been reset successfully.'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User {username} does not exist.'))


# command to run the code
# python manage.py reset_password your_superuser_username new_secure_password