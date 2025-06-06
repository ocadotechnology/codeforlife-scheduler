"""
© Ocado Group
Created on 22/04/2025 at 16:05:09(+01:00).
"""

from pathlib import Path

from codeforlife import set_up_settings
from src.utils import configure_celery

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

secrets = set_up_settings(BASE_DIR, service_name="scheduler")

# pylint: disable-next=wildcard-import,unused-wildcard-import,wrong-import-position,ungrouped-imports,wrong-import-order
from codeforlife.settings import *

SECRET_KEY = secrets.SECRET_KEY

configure_celery()
