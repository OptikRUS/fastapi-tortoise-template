# Шаблон приложения на tortoise ORM

Установка зависимостей:
`pip install -r requirements.txt `

Добавить в .env список username, которые станут админами при регистрации (django по умолчанию):
`SUPER_USERS=["django", "admin", "superuser"]`

Запуск проекта:
`python run.py`

Открыть в браузере:
`http://127.0.0.1:8000/docs`

***

Запуск проекта в контейнере:
`docker-compose up --build -d`

Открыть в браузере:
`http://0.0.0.0:8000/docs`