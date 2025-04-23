"""
© Ocado Group
Created on 22/04/2025 at 16:39:42(+01:00).
"""

import os
import typing as t

from celery.schedules import crontab, solar
from codeforlife.tasks import get_local_sqs_url
from settings import (
    AWS_REGION,
    CELERY_BEAT_SCHEDULE,
    CELERY_BROKER_TRANSPORT_OPTIONS,
    CELERY_TASK_ROUTES,
    ENV,
)


class TaskSchedule(t.TypedDict):
    """A beat schedule.

    https://docs.celeryq.dev/en/v5.4.0/userguide/periodic-tasks.html
    """

    task: str
    schedule: t.Union[int, crontab, solar]
    args: t.NotRequired[t.Tuple[t.Any, ...]]
    kwargs: t.NotRequired[t.Dict[str, t.Any]]


TaskSchedules = t.Dict[str, TaskSchedule]


class TaskRoute(t.TypedDict):
    """A task route.

    https://docs.celeryq.dev/en/v5.4.0/userguide/routing.html
    """

    queue: str


TaskRoutes = t.Dict[str, TaskRoute]


class PredefinedQueue(t.TypedDict):
    """A predefined SQS queue.

    https://docs.celeryq.dev/en/v5.4.0/getting-started/backends-and-brokers/sqs.html#predefined-queues
    """

    url: str


PredefinedQueues = t.Dict[str, PredefinedQueue]


def configure_celery(service_task_schedules: t.Dict[str, TaskSchedules]):
    """Configure Celery by adding each service's:
    1. Predefined SQS queue.
    2. Task schedules.
    3. Task routes.

    Args:
        service_task_schedules: The name and task schedules for each service.
    """

    celery_beat_schedule = t.cast(TaskSchedules, CELERY_BEAT_SCHEDULE)
    celery_task_routes = t.cast(TaskRoutes, CELERY_TASK_ROUTES)
    predefined_queues = t.cast(
        PredefinedQueues, CELERY_BROKER_TRANSPORT_OPTIONS["predefined_queues"]
    )

    for service, task_schedules in service_task_schedules.items():
        # Add beat schedule.
        for name, task_schedule in task_schedules.items():
            task_schedule["task"] = f"{service}.{task_schedule['task']}"
            celery_beat_schedule[f"{service}.{name}"] = task_schedule

        # Add task route.
        celery_task_routes[f"{service}.*"] = {"queue": service}

        # Add predefined queue.
        predefined_queues[service] = {
            "url": (
                os.environ[f"{service.upper()}_SQS_URL"]
                if ENV != "local"
                else get_local_sqs_url(AWS_REGION, service)
            )
        }
