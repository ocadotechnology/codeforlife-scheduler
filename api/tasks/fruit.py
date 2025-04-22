"""
© Ocado Group
Created on 04/04/2025 at 15:47:15(+01:00).
"""

from codeforlife.tasks import shared_task
from django.utils import timezone

from ..models import Fruit


@shared_task
def delete_expired():
    """Delete fruits that have passed their expiry date."""
    Fruit.objects.filter(expires_on__lt=timezone.now()).delete()
