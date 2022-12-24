# установка python 3.11 с официального докерхаба
FROM python:3.11.0rc2

# хост базы данных для докера
ENV DATABASE_HOST=database
# хост сайта
ENV SITE_HOST=0.0.0.0

# установка рабочей директории
WORKDIR /

# установка зависимостей
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# копирование проекта
COPY . .