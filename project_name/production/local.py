# Copyright 2024 ITCase (info@itcase.pro)

# ****************************************************************
# DJANGO

ALLOWED_HOSTS = [".{{ project_name }}.example.com"]
DEBUG = False
from .core import TEMPLATES  # noqa
TEMPLATES[0]["OPTIONS"].update({"debug": DEBUG})

# DATABASES
from .core import DATABASES  # noqa
DATABASES["default"]["PASSWORD"] =

# EMAIL
DEFAULT_FROM_EMAIL = "webmaster@localhost"
EMAIL_HOST = "localhost"
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

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
