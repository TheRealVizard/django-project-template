"""
This is the settings file that you use when you're deploying your project.
"""


# flake8: noqa
from {{ project_name }}.settings.base import *

ALLOWED_HOSTS = ["*"]

DEBUG = False


STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
