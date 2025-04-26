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
            "task": "src.tasks.session.clear",
            "schedule": crontab(hour=16),
        }
    },
    "portal": {
        # session
        "clear_sessions": {
            "task": "src.sso.tasks.session.clear",
            "schedule": crontab(hour=16),
        },
        # user
        "send_1st_verify_email_reminder": {
            "task": "src.api.tasks.user.send_verify_email_reminder",
            "schedule": crontab(hour=16),
            "kwargs": {
                "days": 7,
                "campaign_name": "Verify new user email - first reminder",
            },
        },
        "send_2nd_verify_email_reminder": {
            "task": "src.api.tasks.user.send_verify_email_reminder",
            "schedule": crontab(hour=16),
            "kwargs": {
                "days": 14,
                "campaign_name": "Verify new user email - second reminder",
            },
        },
        "anonymize_users_with_unverified_emails": {
            "task": "src.api.tasks.user.anonymize_unverified_emails",
            "schedule": crontab(hour=16),
        },
        "send_1st_inactivity_email_reminder": {
            "task": "src.api.tasks.user.send_inactivity_email_reminder",
            "schedule": crontab(hour=16),
            "kwargs": {
                "days": 730,
                "campaign_name": "Inactive users on website - first reminder",
            },
        },
        "send_2nd_inactivity_email_reminder": {
            "task": "src.api.tasks.user.send_inactivity_email_reminder",
            "schedule": crontab(hour=16),
            "kwargs": {
                "days": 973,
                "campaign_name": "Inactive users on website - second reminder",
            },
        },
        "send_final_inactivity_email_reminder": {
            "task": "src.api.tasks.user.send_inactivity_email_reminder",
            "schedule": crontab(hour=16),
            "kwargs": {
                "days": 1065,
                "campaign_name": "Inactive users on website - final reminder",
            },
        },
    },
}
