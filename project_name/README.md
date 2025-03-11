# {{ project_name }}

## Разработка

Активируем [pre-commit](https://github.com/pre-commit/pre-commit): `pre-commit install`

### Docker Compose

Запуск через [docker compose](https://docs.docker.com/compose/):

* [устанавливаем Docker](https://docs.docker.com/engine/install/)
* [добавляем ITCase-пакеты](/docker-compose/django/itcase/README.md)
* [добавляем дамп базы](/docker-compose/postgres/init/README.md)(если он есть)
* копируем файл настроек `cp docker-compose/django/settings.local.py settings/local.py`
* запускаем командой `docker compose up`
* открываем в браузере адрес `http://localhost:8000`
* *дополнительно:*
    - при необходимости создаём суперпользователя `docker compose exec -it django poetry run python manage.py createsuperuser admin`
    - запускаем тесты `docker compose exec -it django poetry run pytest`
    - по умолчанию, не выполняются management-команды в cron'е — для их запуска нужно раскоментировать сервис `cron` в [docker-compose.yml](/docker-compose.yml)
