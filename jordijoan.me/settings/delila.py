from .dev import *

# Media folder inside the site folder when sync to delila
MEDIA_ROOT = join(PROJECT_ROOT, SITE_NAME, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SITE_NAME,
        'USER': 'postgres',
        'HOST': '10.0.0.10',  # Set to empty string for localhost.
        'PORT': '5432',  # Set to empty string for default.
    }
}

try:
    from .local import *
except ImportError:
    pass
