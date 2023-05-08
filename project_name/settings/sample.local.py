# Copyright 2023 ITCase (info@itcase.pro)
#
# Settings for local development. Not for production!

# ****************************************************************
# DJANGO

from .caches import CACHES  # noqa
for cache in CACHES:
    CACHES[cache]['LOCATION'] = CACHES[cache]['LOCATION'].replace(
        '127.0.0.1', '192.168.1.21')

# DATABASES
from .core import DATABASES  # noqa
DATABASES['default']['HOST'] = '192.168.1.21'
DATABASES['default']['PASSWORD'] =

# DEBUG
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
ALLOWED_HOSTS = ['*']
DEBUG = True
INTERNAL_IPS = ('127.0.0.1', 'localhost')
from .core import TEMPLATES  # noqa
TEMPLATES[0]['OPTIONS'].update({'debug': DEBUG})

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# STATIC
from .core import STATIC_ROOT, STATICFILES_DIRS  # noqa
STATICFILES_DIRS.append(STATIC_ROOT)
STATIC_ROOT = None

# ****************************************************************
# THIRD-PARTY

# Django CORS Headers
# https://github.com/adamchainz/django-cors-headers
# required for NextJS frontend
try:
    import corsheaders  # noqa
    from .core import INSTALLED_APPS, MIDDLEWARE  # noqa
    INSTALLED_APPS.append('corsheaders')
    MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
    CORS_ALLOW_ALL_ORIGINS = True
except ImportError:
    pass

# Django RQ
# https://github.com/rq/django-rq
from .rq import RQ_QUEUES  # noqa
# run all queues in synchronous mode
for queueConfig in RQ_QUEUES.values():
    queueConfig['ASYNC'] = False
