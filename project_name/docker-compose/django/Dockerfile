FROM python:3.12-slim

# ****************************************************************

LABEL org.opencontainers.image.authors="ITCase (info@itcase.pro)"

# ****************************************************************

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ****************************************************************

RUN apt-get update && apt-get install --no-install-recommends -y wait-for-it

# ****************************************************************
# CRON

RUN apt-get update && apt-get install --no-install-recommends -y cron \
    && chmod u+s /usr/sbin/cron

# ****************************************************************

RUN pip install poetry

RUN useradd --create-home --user-group --shell /bin/bash project

RUN mkdir /project
WORKDIR /project

# копируем файлы для установки зависимостей
COPY poetry.lock pyproject.toml ./
COPY docker-compose/django/itcase docker-compose/django/itcase

RUN chown -R project:project /project

USER project

# устанавливаем зависимости
RUN poetry install --no-root --without=itcase,prod \
    && poetry run pip install python-dotenv ipdb ptpython \
    && poetry run pip install -e docker-compose/django/itcase/itcase-common

# ****************************************************************

# копируем входной скрипт
COPY docker-compose/django/entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
