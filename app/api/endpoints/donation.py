from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.donation import donation_crud
from app.schemas.donation import (
    DonationCreate, DonationUserDB, DonationDB
)

router = APIRouter()


@router.get('/', response_model=list[DonationDB])
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """
    Возвращает список всех пожертвований.
    """
    donations = await donation_crud.get_multi(session)
    return donations
