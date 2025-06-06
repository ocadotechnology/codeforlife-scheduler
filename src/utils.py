"""
© Ocado Group
Created on 22/04/2025 at 16:39:42(+01:00).
"""

import os
import typing as t

from codeforlife.tasks import get_local_sqs_url

from .schedules import SCHEDULES

if t.TYPE_CHECKING:
    from .types import PredefinedQueues, TaskRoutes, TaskSchedules


def configure_celery():
    """Configure Celery by adding each service's:
    1. Predefined SQS queue.
    2. Task schedules.
    3. Task routes.

    https://docs.celeryq.dev/en/v5.4.0/userguide/configuration.html
    https://docs.celeryq.dev/en/v5.4.0/getting-started/backends-and-brokers/sqs.html

    Args:
        service_task_schedules: The name and task schedules for each service.
    """

    # pylint: disable-next=import-outside-toplevel
    import settings

    predefined_queues: "PredefinedQueues" = {}
    beat_schedule: "TaskSchedules" = {}
    task_routes: "TaskRoutes" = {}

    for service, task_schedules in SCHEDULES.items():
        # Add beat schedule.
        for name, task_schedule in task_schedules.items():
            beat_schedule[f"{service}.{name}"] = {
                **task_schedule,
                "task": f"{service}.{task_schedule['task']}",
            }

        # Add task route.
        task_routes[f"{service}.*"] = {"queue": service}

        # Add predefined queue.
        predefined_queues[service] = {
            "url": (
                os.environ[f"{service.replace('-', '_').upper()}_SQS_URL"]
                if settings.ENV != "local"
                else get_local_sqs_url(
                    t.cast(str, settings.AWS_REGION), service
                )
            )
        }

    settings.CELERY_BROKER_TRANSPORT_OPTIONS["predefined_queues"] = (
        predefined_queues  # type: ignore[assignment]
    )
    settings.CELERY_BEAT_SCHEDULE = beat_schedule  # type: ignore[attr-defined]
    settings.CELERY_TASK_ROUTES = task_routes  # type: ignore[attr-defined]
