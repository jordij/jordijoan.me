from .base import *

# Analytics stuff
GOOGLE_TAG_MANAGER = False
GOOGLE_ANALYTICS_KEY = False

DEBUG = True
TEMPLATE_DEBUG = True

COMPRESS_ENABLED = False

DATABASES['default']['PASSWORD'] = ''

# To have fake email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.db',
    }
}

# As required by debug_toolbar
INTERNAL_IPS = (
   '10.0.2.2',
   '127.0.0.1',
)

INSTALLED_APPS += (
    'debug_toolbar',
)

CACHE_MIDDLEWARE_SECONDS = 0

INSTALLED_APPS = INSTALLED_APPS + (
    'wagtail.contrib.wagtailstyleguide',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
) + MIDDLEWARE_CLASSES
