from fastapi import APIRouter, Depends

from services.users import current_active_user
from db.tables import User
from db.db import create_db_and_tables

router = APIRouter()

@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@router.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()