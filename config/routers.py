from fastapi import APIRouter


def get_routers() -> list[APIRouter]:
    from src.users.api import users_router
    from src.admins.api import admins_router
    from src.library.api import authors_router, books_router, genres_router

    routers: list[APIRouter] = list()

    # добавляем сюда роутеры
    routers.append(users_router)
    routers.append(admins_router)
    routers.append(authors_router)
    routers.append(genres_router)
    routers.append(books_router)

    return routers
