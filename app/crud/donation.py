from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):

    async def get_user_donations(
            self,
            user: User,
            session: AsyncSession,
    ):
        db_objs = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return db_objs.scalars().all()

    async def create(
        self,
        obj_in,
        session: AsyncSession,
        user: User,
    ):
        obj_in_data = obj_in.dict()
        obj_in_data['user_id'] = user.id
        db_obj = Donation(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


donation_crud = CRUDDonation(Donation)
