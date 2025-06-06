"""
© Ocado Group
Created on 22/04/2025 at 16:05:09(+01:00).
"""

import typing as t
from pathlib import Path

from codeforlife import set_up_settings
from src.utils import configure_celery

if t.TYPE_CHECKING:
    from src.types import TaskRoutes, TaskSchedules

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

secrets = set_up_settings(BASE_DIR, service_name="scheduler")

# pylint: disable-next=wildcard-import,unused-wildcard-import,wrong-import-position,ungrouped-imports,wrong-import-order
from codeforlife.settings import *

SECRET_KEY = secrets.SECRET_KEY

# Celery
# https://docs.celeryq.dev/en/v5.4.0/userguide/configuration.html
# https://docs.celeryq.dev/en/v5.4.0/getting-started/backends-and-brokers/sqs.html

# WARN: Do not set - leave empty.
# These dictionaries are populated at runtime by a utility function.
CELERY_BROKER_TRANSPORT_OPTIONS["predefined_queues"] = {}
CELERY_BEAT_SCHEDULE: "TaskSchedules" = {}
CELERY_TASK_ROUTES: "TaskRoutes" = {}

configure_celery()
