"""
© Ocado Group
Created on 04/07/2024 at 11:42:00(+01:00).

Django settings for api.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

from codeforlife import set_up_settings
from codeforlife.tasks import CeleryBeatScheduleBuilder

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

secrets = set_up_settings(BASE_DIR, service_name="REPLACE_ME")

# pylint: disable-next=wildcard-import,unused-wildcard-import,wrong-import-position
from codeforlife.settings import *

SECRET_KEY = secrets.SECRET_KEY

# Celery
# https://docs.celeryq.dev/en/v5.4.0/userguide/configuration.html

CELERY_BEAT_SCHEDULE = CeleryBeatScheduleBuilder(
    delete_expired_fruits={
        "task": "api.tasks.fruit.delete_expired",
        "schedule": CeleryBeatScheduleBuilder.crontab(hour=16),
    },
)
