from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "first_name" VARCHAR(50),
    "last_name" VARCHAR(50),
    "patronymic_name" VARCHAR(50),
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "phone" VARCHAR(15)  UNIQUE,
    "password" VARCHAR(128),
    "is_active" BOOL NOT NULL  DEFAULT True,
    "is_approved" BOOL NOT NULL  DEFAULT False,
    "is_superuser" BOOL NOT NULL  DEFAULT False,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE "users" IS 'Модель пользователя';
CREATE TABLE IF NOT EXISTS "authors" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "patronymic_name" VARCHAR(50),
    "date_of_birth" DATE,
    "date_of_death" DATE,
    CONSTRAINT "uid_authors_first_n_029fae" UNIQUE ("first_name", "last_name")
);
COMMENT ON TABLE "authors" IS 'Модель автора';
CREATE TABLE IF NOT EXISTS "books" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(200) NOT NULL UNIQUE,
    "summary" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "author_id" INT REFERENCES "authors" ("id") ON DELETE SET NULL
);
COMMENT ON TABLE "books" IS 'Модель книги';
CREATE TABLE IF NOT EXISTS "genres" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL UNIQUE
);
COMMENT ON TABLE "genres" IS 'Модель жанра книги';
CREATE TABLE IF NOT EXISTS "books_genres" (
    "books_id" INT NOT NULL REFERENCES "books" ("id") ON DELETE SET NULL,
    "genre_id" INT NOT NULL REFERENCES "genres" ("id") ON DELETE SET NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
