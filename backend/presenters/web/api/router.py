from fastapi.routing import APIRouter

from backend.presenters.web.api import auth, user

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["Пользователи"])
api_router.include_router(auth.router, prefix="/auth", tags=["Авторизация"])
