"""
© Ocado Group
Created on 04/04/2025 at 15:52:29(+01:00).
"""

from datetime import timedelta

from codeforlife.tests import CeleryTestCase
from django.utils import timezone

from ..models import Fruit


# pylint: disable-next=missing-class-docstring
class TestFruitTasks(CeleryTestCase):
    fixtures = ["fruits"]

    def test_delete_expired_fruits(self):
        """All expired fruits are deleted."""
        # Assert some fruits exist.
        assert Fruit.objects.exists()
        # Update all fruits to have expired yesterday.
        Fruit.objects.update(expires_on=timezone.now() - timedelta(days=1))
        # Run task to delete all expired fruits.
        self.apply_periodic_task("delete_expired_fruits")
        # Assert all fruits have been deleted.
        assert not Fruit.objects.exists()
