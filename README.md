# Шаблон приложения на tortoise ORM

Установка зависимостей:
`pip install -r requirements.txt `

Добавить в .env список username, которые станут админами при регистрации (django по умолчанию):
`SUPER_USERS=["django", "admin", "superuser"]`

***

1. Запуск проекта в контейнере:
`docker-compose up --build -d`

2. Открыть в браузере:
`http://0.0.0.0:8000/docs`

***

1. Запуск проекта локально:
`python run.py`

2. Открыть в браузере:
`http://127.0.0.1:8000/docs`