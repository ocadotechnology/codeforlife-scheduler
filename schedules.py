"""
© Ocado Group
Created on 24/04/2025 at 17:10:47(+01:00).
"""

from utils import ServiceTaskSchedules


SCHEDULES: ServiceTaskSchedules = {
    "contributor": {
        "clear_sessions": {
            "task": "api.tasks.session.clear",
            "schedule": 5,  # crontab(hour=16),
        }
    }
}


if __name__ == "__main__":
    print(",".join(SCHEDULES.keys()))
