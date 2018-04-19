from .base import *
import djcelery

# Analytics stuff
GOOGLE_TAG_MANAGER = False
GOOGLE_ANALYTICS_KEY = False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = True
COMPRESS_ENABLED = True

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

# Static folder ready for production mode
STATIC_ROOT = join(DJANGO_ROOT, 'static')
STATICFILES_DIRS = ()

# Add apps
INSTALLED_APPS += (
    'djcelery',
    'djcelery_email'
)

# Celery
djcelery.setup_loader()
# Enables error emails.
CELERY_SEND_TASK_ERROR_EMAILS = True

BROKER_URL = 'redis://'
CELERY_RESULT_BACKEND = 'redis://'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.db',
    }
}

# Use Redis as the cache backend for extra performance

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'KEY_PREFIX': SITE_NAME,
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
) + MIDDLEWARE_CLASSES + (
    'django.middleware.cache.FetchFromCacheMiddleware',
)

# Make sure we include the needed Middleware apps
# Excluding logged in (admin) requests
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(DJANGO_ROOT, 'logs/%s.log' % SITE_NAME),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 50,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins'],
            'propagate': True,
            'level': 'ERROR',
        },
        'core': {
            'handlers': ['file', 'mail_admins'],
            'propagate': True,
            'level': 'ERROR',
        }
    }
}

try:
    from .local import *
except ImportError:
    pass
