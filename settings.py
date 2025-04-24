"""
© Ocado Group
Created on 22/04/2025 at 16:05:09(+01:00).
"""

import typing as t

# pylint: disable=unused-import
from codeforlife.settings.custom import ENV
from codeforlife.settings.third_party import (
    AWS_REGION,
    CELERY_BROKER_TRANSPORT_OPTIONS,
    CELERY_BROKER_URL,
    CELERY_TIMEZONE,
)

# pylint: enable=unused-import

if t.TYPE_CHECKING:
    from utils import TaskRoutes, TaskSchedules

# Celery
# https://docs.celeryq.dev/en/v5.4.0/userguide/configuration.html
# https://docs.celeryq.dev/en/v5.4.0/getting-started/backends-and-brokers/sqs.html

# WARN: Do not set - leave empty.
# These dictionaries are populated at runtime by a utility function.
CELERY_BROKER_TRANSPORT_OPTIONS["predefined_queues"] = {}
CELERY_BEAT_SCHEDULE: "TaskSchedules" = {}
CELERY_TASK_ROUTES: "TaskRoutes" = {}
