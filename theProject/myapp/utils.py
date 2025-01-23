from datetime import timedelta

from django.utils import timezone

from .models import Cart


def cleanup_expired_cart_items():
    expiration_time = timezone.now() - timedelta(minutes=30)
    Cart.objects.filter(created_at__lt=expiration_time).delete()
    print("session deleted")
