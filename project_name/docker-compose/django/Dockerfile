FROM python:3.12-slim

# ****************************************************************

LABEL org.opencontainers.image.authors="ITCase (info@itcase.pro)"

# ****************************************************************

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ****************************************************************

RUN apt-get update && apt-get install --no-install-recommends -y wait-for-it

# ****************************************************************

# создаём рабочий каталог
RUN mkdir /project
WORKDIR /project/

# копируем файлы для установки зависимостей
COPY poetry.lock pyproject.toml /project/

# устанавливаем зависимости
RUN pip install poetry \
    && poetry install --no-root --without=itcase,prod \
    && poetry run pip install python-dotenv ipdb ptpython

# утсанавливаем ITCase Common
COPY docker-compose/django/itcase/itcase-common /itcase-common
RUN poetry run pip install -e /itcase-common

# ****************************************************************
# CRON

RUN apt-get update \
    && apt-get install --no-install-recommends -y cron \
    && touch /var/log/cron.log

# ****************************************************************

# копируем входной скрипт
COPY docker-compose/django/entrypoint.sh /docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]