from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise


def init_app() -> FastAPI:
    from config import app_config
    app = FastAPI(**app_config)

    return app


def init_cors(application: FastAPI) -> None:
    from config import cors_config
    application.add_middleware(CORSMiddleware, **cors_config)


def init_routers(application: FastAPI) -> None:
    from config.routers import get_routers

    for router in get_routers():
        application.include_router(router)


def init_database(application: FastAPI) -> None:
    from config import database_config

    register_tortoise(
        application,
        db_url=database_config.get('db_url').format(**database_config),
        modules={"models": ["users.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
