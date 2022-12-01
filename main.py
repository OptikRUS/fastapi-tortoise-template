from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from users.api import users_router
from admins.api import admins_router

from config import app_config, database_config, site_config

app = FastAPI(**app_config)

register_tortoise(
    app,
    db_url=database_config.get('database_url').format(**database_config),
    modules={"models": ["users.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(users_router)
app.include_router(admins_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", **site_config)
