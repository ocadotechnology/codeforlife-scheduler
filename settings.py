"""
© Ocado Group
Created on 22/04/2025 at 16:05:09(+01:00).
"""

import typing as t

# pylint: disable=unused-import
from celery.schedules import crontab
from codeforlife.settings.custom import ENV
from codeforlife.settings.third_party import (
    AWS_REGION,
    CELERY_BROKER_TRANSPORT_OPTIONS,
    CELERY_BROKER_URL,
    CELERY_TIMEZONE,
)

# pylint: enable=unused-import

if t.TYPE_CHECKING:
    from src.types import TaskRoutes, TaskSchedules


# Custom

SCHEDULES: t.Dict[str, "TaskSchedules"] = {
    "contributor": {
        "clear_sessions": {
            "task": "api.tasks.session.clear",
            "schedule": crontab(hour=16),
        }
    },
    "portal": {
        "clear_sessions": {
            "task": "src.sso.tasks.session.clear",
            "schedule": crontab(hour=16),
        }
    }
}

# Celery
# https://docs.celeryq.dev/en/v5.4.0/userguide/configuration.html
# https://docs.celeryq.dev/en/v5.4.0/getting-started/backends-and-brokers/sqs.html

# WARN: Do not set - leave empty.
# These dictionaries are populated at runtime by a utility function.
CELERY_BROKER_TRANSPORT_OPTIONS["predefined_queues"] = {}
CELERY_BEAT_SCHEDULE: "TaskSchedules" = {}
CELERY_TASK_ROUTES: "TaskRoutes" = {}
