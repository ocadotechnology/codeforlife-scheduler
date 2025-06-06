"""
© Ocado Group
Created on 25/04/2025 at 08:45:32(+01:00).
"""

import typing as t
from unittest import TestCase
from unittest.mock import patch

from codeforlife.tasks import get_local_sqs_url

from .schedules import SCHEDULES
from .types import ServiceTaskSchedules
from .utils import configure_celery


# pylint: disable-next=missing-class-docstring
class TestUtils(TestCase):
    def test_configure_celery(self):
        """Can successfully configure Celery to schedule tasks per service."""

        schedules: ServiceTaskSchedules = {
            "service1": {
                "schedule1": {
                    "task": "path.to.task",
                    "schedule": 1,
                },
            },
        }

        with patch.dict(SCHEDULES, schedules, clear=True):
            configure_celery()

        # pylint: disable-next=import-outside-toplevel
        from settings import (  # type: ignore[attr-defined]
            AWS_REGION,
            CELERY_BEAT_SCHEDULE,
            CELERY_BROKER_TRANSPORT_OPTIONS,
            CELERY_TASK_ROUTES,
        )

        self.assertDictEqual(
            CELERY_BEAT_SCHEDULE,
            {
                "service1.schedule1": {
                    "task": "service1.path.to.task",
                    "schedule": 1,
                },
            },
        )
        self.assertDictEqual(
            CELERY_BROKER_TRANSPORT_OPTIONS,
            {
                **CELERY_BROKER_TRANSPORT_OPTIONS,
                "predefined_queues": {
                    "service1": {
                        "url": get_local_sqs_url(
                            t.cast(str, AWS_REGION), "service1"
                        )
                    }
                },
            },
        )
        self.assertDictEqual(
            CELERY_TASK_ROUTES,
            {"service1.*": {"queue": "service1"}},
        )
