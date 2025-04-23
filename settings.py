"""
© Ocado Group
Created on 22/04/2025 at 16:05:09(+01:00).
"""

# pylint: disable=unused-import
from codeforlife.settings.custom import ENV
from codeforlife.settings.third_party import (
    AWS_REGION,
    CELERY_BROKER_TRANSPORT_OPTIONS,
    CELERY_BROKER_URL,
    CELERY_TIMEZONE,
)

# pylint: enable=unused-import


# Celery
# https://docs.celeryq.dev/en/v5.4.0/userguide/configuration.html
# https://docs.celeryq.dev/en/v5.4.0/getting-started/backends-and-brokers/sqs.html

CELERY_BROKER_TRANSPORT_OPTIONS["predefined_queues"] = {}
CELERY_BEAT_SCHEDULE = {}
CELERY_TASK_ROUTES = {}
