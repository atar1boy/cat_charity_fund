from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import get_async_session, current_user, current_superuser
from app.crud import donation_crud
from app.models import User
from app.schemas import (
    DonationCreate, DonationUserDB, DonationDB
)


router = APIRouter()


@router.get(
        '/',
        response_model=list[DonationDB],
        dependencies=[Depends(current_superuser)],
    )
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """
    Возвращает список всех пожертвований.
    """
    donations = await donation_crud.get_multi(session)
    return donations


@router.get(
        '/my',
        response_model=list[DonationUserDB],
        dependencies=[Depends(current_user)],
    )
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """
    Возвращает список всех пожертвований пользователя.
    """
    donations = await donation_crud.get_user_donations(user, session)
    return donations


@router.post(
        '/',
        response_model=DonationUserDB,
        dependencies=[Depends(current_user)]
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    new_donation = await donation_crud.create(
        donation, session, user
    )
    return new_donation
