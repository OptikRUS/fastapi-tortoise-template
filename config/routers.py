from fastapi import APIRouter


def get_routers() -> list[APIRouter]:
    from users import users_router
    from admins import admins_router

    routers: list[APIRouter] = list()

    # добавляем сюда роутеры
    routers.append(users_router)
    routers.append(admins_router)

    return routers
