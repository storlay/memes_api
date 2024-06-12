<h1 align="center">API: Работа с коллекцией мемов и S3 хранилищем 🙂</h1>

<div align="center">

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Postgres](https://img.shields.io/badge/postgres-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![MinIO](https://img.shields.io/badge/minio-00A3E0?style=for-the-badge&logo=minio&logoColor=white)](https://min.io/)
[![aiobotocore](https://img.shields.io/badge/aiobotocore-477D94?style=for-the-badge&logo=awslambda&logoColor=white)](https://github.com/aio-libs/aiobotocore)
[![Gunicorn](https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![Poetry](https://img.shields.io/badge/poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)


</div>

Выполнено в рамках [тестового задания](https://docs.google.com/document/d/1PC4WtKXcGEqRaklby5XI2S7FZy_AP6J37dH0ENsMxfw)

- `app` — API для работы с мемами
- `media` — Сервис для работы с изображениями (S3)

## Описание

Асинхронный REST API сервис для работы с коллекцией мемов. 
Хранения изображений — [MinIO](https://min.io/).
Асинхронный доступ к хранилищу — [aiobotocore](https://github.com/aio-libs/aiobotocore).

## Функциональность

- **GET `/memes`**:
    - Получить список всех мемов (с пагинацией).

- **GET `/memes/{id}`**:
    - Получить мем по его ID.

- **POST `/memes`**:
    - Добавить новый мем (с картинкой и текстом).

- **PUT `/memes/{id}`**:
    - Обновить существующий мем по его ID.

- **DELETE `/memes/{id}`**:
    - Удалить мем по его ID.

## Установка и запуск

1. Склонируйте репозиторий:

```
git clone https://github.com/storlay/memes_api.git
```

2. В корне проекта создайте и заполните файл `.env`


3. Запустите проект с помощью Docker Compose:

```
docker-compose up --build
```

4. После успешного запуска сервисов, приложение будет доступно по следующим адресам:
    - API для работы с мемами: http://127.0.0.1:8000
    - Сервис для загрузки изображений: http://127.0.0.1:8001
    - MinIO: http://127.0.0.1:9000 (для доступа к MinIO консоли)

## Использование

Документация API для работы с мемами доступна по адресу:

- http://127.0.0.1:8000/docs

Документация сервиса для загрузки изображений доступна по адресу:

- http://127.0.0.1:8001/docs

Для использования сервиса для загрузки изображений необходимо авторизоваться,
по умолчанию данные для входа идентичны данным для MinIO
(`MINIO_ROOT_USER`, `MINIO_ROOT_PASSWORD`)*
> *Задаются в файле `.env`


