# Cервис авторизации и новостей с комментариями и лайками

## Описание

Проект описывает работу сервиса новостей с комментариями и лайками.
Пользователи могут создавать новости, комментировать их и ставить лайки новостям.
У каждого из пользователей может быть роль либо админа (позволяет логинится в админке
сервиса), либо роль обычного пользователя.

### Документация API

Документация API в формате Swagger сохранена в файле Swagger News and Authorization Service.yaml
в корневой папке проекта.

### Технологии

- Python 3.11
- Django 5.0.6
- Django REST Framework 3.15.1
- DRF-Spectacular 0.27.2
- PostgreSQL 16.3
- SimpleJWT 5.3.1
- dotenv 1.0.1
- gunicorn 22.0
- nginx 1.25.3
- docker


## Запуск проекта локально

- клонировать репозиторий

```
git clone git@github.com:SunnyInHouse/news_service.git
```

- в директории  news_and_authorization_service создать файл .env и наполнить его по примеру .env_sample

```
DEBUG=False
DJANGO_SECRET_KEY=django-secret

DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=postgres-news-service
DB_PORT=5432
```

#### Предупреждение

```
Если вы используете Windows, убедитесь, что файл run_app.sh имеет формат конца строки LF
```

- перейти в директорию infra

```
cd infra 
```

- запустить сборку контейнеров:

```
docker-compose up -d
```

- проект доступен по адресу:

```
http://localhost/api/v1
```
- документация доступна по адресу:

```
http://localhost/api/doc/swagger/v1/
http://localhost/api/doc/v1/download/
```

- после запуска проекта в базе данных уже есть пользователи:

1. администратор (username - admin, password - admin)
2. обычный пользователь (username - Sandy, password - User128590)
 
## Автор проекта

[SunnyInHouse](https://github.com/SunnyInHouse)

