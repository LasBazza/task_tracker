# Task tracker

Приложение - API журнала задач, содержит следующие сущности: 
- User (Пользователь)
- Task (Задача)

Реализована система аутентификации по JWT токену. Реализованы CRUD операции для сущности задач, система пермишенов.

## Стек технологий и библиотек

- python 3
- django 4.0.5
- djangorestframework 3.13.1
- djangorestframework-simplejwt
- docker-compose
- nginx
- postgreSQL
- gunicorn

## Запуск приложения

#### Склонировать репозиторий
#### Создать файл .env

В папке _/task_tracker/config_ создать файл _.env_, по образцу файла _.env.dist_, находящегося в той же папке.

#### Запуск docker-compose

Из корневой папки проекта выполнить команду в терминале команду 

```docker-compose up```

#### Готово!

Базовый URL проекта _http://127.0.0.1/api/_. 

Документация к API по адресу _http://127.0.0.1/swagger/_. 

Есть админ панель django _http://127.0.0.1/admin/_. Создать суперпользователя можно, выполнив из корневой папки проекта команду

```docker-compose exec web python manage.py createsuperuser```
