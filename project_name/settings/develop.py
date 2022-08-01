
"""
This is the settings file that you use when you're working on the project locally.
"""

# flake8: noqa
from {{ project_name }}.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

THIRD_PARTY_APPS += ["django_linear_migrations", "django_extensions", "debug_toolbar"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ project_name }}/howto/static-files/

STATIC_URL = "/{{ project_name }}/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
