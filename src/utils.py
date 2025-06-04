"""
© Ocado Group
Created on 22/04/2025 at 16:39:42(+01:00).
"""

import os
import typing as t

from codeforlife.tasks import get_local_sqs_url

from .schedules import SCHEDULES

if t.TYPE_CHECKING:
    from .types import PredefinedQueues


def configure_celery():
    """Configure Celery by adding each service's:
    1. Predefined SQS queue.
    2. Task schedules.
    3. Task routes.

    Args:
        service_task_schedules: The name and task schedules for each service.
    """

    # pylint: disable-next=import-outside-toplevel
    from settings import (  # type: ignore[attr-defined]
        AWS_REGION,
        CELERY_BEAT_SCHEDULE,
        CELERY_BROKER_TRANSPORT_OPTIONS,
        CELERY_TASK_ROUTES,
        ENV,
    )

    predefined_queues = t.cast(
        "PredefinedQueues", CELERY_BROKER_TRANSPORT_OPTIONS["predefined_queues"]
    )

    for service, task_schedules in SCHEDULES.items():
        # Add beat schedule.
        for name, task_schedule in task_schedules.items():
            task_schedule["task"] = f"{service}.{task_schedule['task']}"
            CELERY_BEAT_SCHEDULE[f"{service}.{name}"] = task_schedule

        # Add task route.
        CELERY_TASK_ROUTES[f"{service}.*"] = {"queue": service}

        # Add predefined queue.
        predefined_queues[service] = {
            "url": (
                os.environ[f"{service.replace('-', '_').upper()}_SQS_URL"]
                if ENV != "local"
                else get_local_sqs_url(AWS_REGION, service)
            )
        }
