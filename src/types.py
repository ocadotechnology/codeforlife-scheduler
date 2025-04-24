"""
© Ocado Group
Created on 24/04/2025 at 21:17:06(+01:00).
"""

import typing as t

if t.TYPE_CHECKING:
    from celery.schedules import crontab, solar


class TaskSchedule(t.TypedDict):
    """A beat schedule.

    https://docs.celeryq.dev/en/v5.4.0/userguide/periodic-tasks.html
    """

    task: str
    schedule: t.Union[int, "crontab", "solar"]
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
