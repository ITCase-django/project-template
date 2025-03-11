#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

wait-for-it "$DJANGO_DATABASE_HOST:$DJANGO_DATABASE_PORT" -t 0
>&2 echo "PostgreSQL is available"

wait-for-it "$DJANGO_REDIS_HOST:$DJANGO_REDIS_PORT" -t 30
>&2 echo "Redis is available"

if [[ "$1" = "cron" ]]; then
    wait-for-it "$DJANGO_HOST:$DJANGO_PORT" -t 0
    >&2 echo "Django is available"
    crontab docker-compose/django/cron && cron && tail -f /var/log/cron.log
elif [[ "$1" = "rqworker" ]]; then
    wait-for-it "$DJANGO_HOST:$DJANGO_PORT" -t 0
    >&2 echo "Django is available"
    poetry run python manage.py rqworker {{ project_name }}_high {{ project_name }}_default {{ project_name }}_low
else
    # накатываем миграции
    poetry run python manage.py migrate
    # запускаем всё в виртуальном окружении
    poetry run "$@"
fi
