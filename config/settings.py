from pydantic import BaseSettings, Field


class SiteSettings(BaseSettings):
    host: str = Field("127.0.0.1", env="SITE_HOST")
    port: int = Field(8000, env="SITE_PORT")
    # reload: bool = Field(True, env="SITE_RELOAD")
    # reload_delay: float = Field(0.25, env="SITE_RELOAD_DELAY")
    log_level: str = Field("info", env="SITE_LOG_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ApplicationSettings(BaseSettings):
    title: str = Field("Fastapi with tortoise ORM template")
    description = Field("Шаблон приложения на tortoise ORM")
    debug: bool = Field(True, env="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DataBaseSettings(BaseSettings):

    # postgres
    # port: str = Field("5432", env="DATABASE_PORT")
    # user: str = Field("postgres", env="DATABASE_USER")
    # host: str = Field("db_app", env="DATABASE_HOST")
    # password: str = Field("postgres", env="DATABASE_PASSWORD")
    # db_name: str = Field("postgres", env="DATABASE_NAME")
    # database_url: str = Field("postgres://{user}:{password}@{host}:{port}/{database}")

    # sqlite
    db_name: str = Field("db_app", env="DATABASE_NAME")
    database_url: str = Field("sqlite://{db_name}.db")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DataBaseUrl(BaseSettings):
    url: str = Field(DataBaseSettings().database_url.format(**DataBaseSettings().dict()))


class DataBaseModels(BaseSettings):
    models: list = Field([
        "users.models",
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
    expires: int = Field(60*60)
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
