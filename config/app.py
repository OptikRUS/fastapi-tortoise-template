from fastapi import FastAPI


def get_fastapi_app() -> FastAPI:
    from config.initializers import init_app, init_cors, init_routers, init_database

    application: FastAPI = init_app()

    init_cors(application)
    init_routers(application)
    init_database(application)

    return application
