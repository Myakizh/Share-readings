from fastapi import APIRouter

from models.schemas import UserCreate, UserRead, UserUpdate
from services.users import auth_backend, fastapi_users

from .sup import router as sup_router
from .temp import router as temp_router
from .auth import router as auth_router

router = APIRouter()

router.include_router(sup_router)
router.include_router(temp_router)
router.include_router(auth_router)

router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)