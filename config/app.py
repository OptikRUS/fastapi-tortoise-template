from fastapi import FastAPI


def get_fastapi_app() -> FastAPI:
    from config.initializers import (
        init_app,
        init_cors,
        init_routers,
        init_database,
        init_exception_handlers
    )

    application: FastAPI = init_app()

    init_cors(application)
    init_routers(application)
    init_database(application)
    init_exception_handlers(application)

    return application
