# Шаблон приложения на tortoise ORM

Установка зависимостей:
`pip install -r requirements.txt `

Добавить в .env список username, которые станут админами при регистрации (django по умолчанию):
`SUPER_USERS=["django", "admin", "superuser"]`

Запуск контейнера базы данных:
`docker-compose up --build -d`

Запуск проекта:
`python run.py`
