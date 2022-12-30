from fastapi import FastAPI


def init_app() -> FastAPI:
    from config import app_config

    app = FastAPI(**app_config)
    return app


def init_cors(application: FastAPI) -> None:
    from fastapi.middleware.cors import CORSMiddleware
    from config import cors_config

    application.add_middleware(CORSMiddleware, **cors_config)


def init_routers(application: FastAPI) -> None:
    from config.routers import get_routers

    for router in get_routers():
        application.include_router(router)


def init_database(application: FastAPI) -> None:
    from tortoise.contrib.fastapi import register_tortoise
    from config import database_config, tortoise_config

    register_tortoise(application, config=database_config, **tortoise_config)


def init_exception_handlers(application: FastAPI) -> None:
    from common.handlers import common_exception_handler
    from common.exceptions.base import BaseHTTPException

    application.add_exception_handler(BaseHTTPException, common_exception_handler)
