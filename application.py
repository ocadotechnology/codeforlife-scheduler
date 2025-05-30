"""
© Ocado Group
Created on 17/04/2025 at 09:40:11(+01:00).

A worker for the celery beat.
"""

from celery import Celery  # isort: skip

import settings
from src.utils import configure_celery


def main():
    """Entry point."""

    configure_celery()

    app = Celery()
    app.config_from_object(settings, namespace="CELERY")
    app.Beat(  # type: ignore[call-arg]
        loglevel="INFO",
    ).run()  # type: ignore[attr-defined]


if __name__ == "__main__":
    main()
