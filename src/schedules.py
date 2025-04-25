"""
© Ocado Group
Created on 24/04/2025 at 21:30:21(+01:00).
"""

import typing as t

from celery.schedules import crontab

if t.TYPE_CHECKING:
    from .types import ServiceTaskSchedules


SCHEDULES: "ServiceTaskSchedules" = {
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
    },
}
