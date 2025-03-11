# Copyright 2025 ITCase (info@itcase.pro)

# Django RQ
# https://github.com/rq/django-rq

from .project import PROJECT_NAME

RQ_QUEUES = {
    f"{PROJECT_NAME}_default": {"USE_REDIS_CACHE": "queue"},
    f"{PROJECT_NAME}_high": {"USE_REDIS_CACHE": "queue"},
    f"{PROJECT_NAME}_low": {"USE_REDIS_CACHE": "queue"},
}
