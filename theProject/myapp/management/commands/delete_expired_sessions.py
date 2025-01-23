# delete_expired_sessions.py
from django.contrib.sessions.models import Session
from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import Cart


class Command(BaseCommand):
    help = 'Delete expired session keys from the Cart table'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_sessions = Session.objects.filter(expire_date__lt=now)
        for session in expired_sessions:
            Cart.objects.filter(session_key=session.session_key).delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted expired session keys'))
