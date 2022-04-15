# Copyright 2022 ITCase (info@itcase.pro)

# ****************************************************************
# DJANGO

ALLOWED_HOSTS = ['.{{ project_name }}.example.com']
DEBUG = False
from .core import TEMPLATES  # noqa
TEMPLATES[0]['OPTIONS'].update({'debug': DEBUG})

# DATABASES
from .core import DATABASES  # noqa
DATABASES['default']['PASSWORD'] =

# EMAIL
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD =
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_PORT = 465
EMAIL_USE_TLS = True

# ****************************************************************
# THIRD-PARTY

# Sentry
# https://docs.sentry.io/
import sentry_sdk  # noqa
from sentry_sdk.integrations.django import DjangoIntegration  # noqa
from sentry_sdk.integrations.rq import RqIntegration  # noqa
sentry_sdk.init(
    dsn=,
    integrations=[DjangoIntegration(), RqIntegration()],
    send_default_pii=True
)
