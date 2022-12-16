from pydantic import BaseSettings, Field


class SiteSettings(BaseSettings):
    host: str = Field("127.0.0.1", env="SITE_HOST")
    port: int = Field(8000, env="SITE_PORT")
    loop: str = Field("asyncio")  # для асинхронного дебага
    log_level: str = Field("info", env="SITE_LOG_LEVEL")
    # reload: bool = Field(True, env="SITE_RELOAD")  # перезагрузка uvicorn
    reload_delay: float = Field(0.25, env="SITE_RELOAD_DELAY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ApplicationSettings(BaseSettings):
    title: str = Field("Fastapi with tortoise ORM template")
    description = Field("Шаблон приложения на tortoise ORM")
    debug: bool = Field(True, env="DEBUG")
    version: str = Field("0.1.0", env="APP_VERSION")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DataBaseSettings(BaseSettings):

    # postgres
    user: str = Field("postgres", env="DATABASE_USER")
    password: str = Field("postgres", env="DATABASE_PASSWORD")
    port: str = Field("5432", env="DATABASE_PORT")
    db_name: str = Field("db_app", env="DATABASE_NAME")
    host: str = Field("localhost", env="DATABASE_HOST")
    database_url: str = Field("postgres://{user}:{password}@{host}:{port}/{db_name}")

    # настройки для sqlite
    # db_name: str = Field("db_app", env="DATABASE_NAME")
    # database_url: str = Field("sqlite://{db_name}.db")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DataBaseUrl(BaseSettings):
    url: str = Field(DataBaseSettings().database_url.format(**DataBaseSettings().dict()))


class DataBaseModels(BaseSettings):
    models: list = Field([
        "users.models",
        "library.models"
    ])


class TortoiseSettings(BaseSettings):
    db_url: str = Field(DataBaseUrl().url)
    modules: dict = Field(DataBaseModels())
    generate_schemas: bool = Field(True, env="TORTOISE_GENERATE_SCHEMAS")
    add_exception_handlers: bool = Field(True, env="DATABASE_EXCEPTION_HANDLERS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class AuthSettings(BaseSettings):
    type: str = Field("Bearer")
    password_time: int = Field(3)
    algorithm: str = Field("HS256")
    expires: int = Field(60*60, env="TOKEN_EXPIRES")  # 1 час
    hasher_deprecated: str = Field("auto")
    hasher_schemes: list[str] = Field(["bcrypt"])
    token_url: str = Field("users/login")

    secret_key: str = Field("secret_key", env="AUTH_SECRET_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class CORSSettings(BaseSettings):
    allow_credentials: bool = Field(True)
    allow_methods: list[str] = Field(["*"])
    allow_headers: list[str] = Field(["*", "Authorization"])
    allow_origins: list[str] = Field(["*"], env="CORS_ORIGINS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class SuperUsersSettings(BaseSettings):
    superusers: list[str] = Field(["django"], env="SUPER_USERS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
