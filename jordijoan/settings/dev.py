from .base import *

# Analytics stuff
GOOGLE_TAG_MANAGER = False
GOOGLE_ANALYTICS_KEY = False

DEBUG = True

COMPRESS_ENABLED = False

DATABASES['default']['PASSWORD'] = ''

# To have fake email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.db',
    }
}

CACHE_MIDDLEWARE_SECONDS = 0

INSTALLED_APPS = INSTALLED_APPS + (
    'wagtail.contrib.wagtailstyleguide',
)
