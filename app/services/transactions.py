from datetime import datetime
from typing import Union
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Donation, CharityProject
from app.crud import CRUDTransactions


class Transactions:

    def __init__(self, model):
        self.model = model

    def get_CRUD(self):
        investment_crud = CRUDTransactions(self.model)
        return investment_crud

    async def investing(
            self,
            obj_in: Union[Donation, CharityProject],
            session: AsyncSession,
    ):
        investment_crud = self.get_CRUD()
        required: int = obj_in.full_amount
        not_invested_objs: list[Union[Donation, CharityProject]] = (
            await investment_crud.get_not_invested_objs(session))

        while not_invested_objs and required:
            obj = not_invested_objs.pop()
            available = obj.full_amount - obj.invested_amount

            if required >= available:
                required -= available
                obj.invested_amount = obj.full_amount
                obj.fully_invested = True
                obj.close_date = datetime.now()

            else:
                obj.invested_amount += required
                required = 0

            session.add(obj)

        if required == 0:
            obj_in.invested_amount = obj_in.full_amount
            obj_in.fully_invested = True
            obj_in.close_date = datetime.now()
        else:
            obj_in.invested_amount = obj_in.full_amount - required

        session.add(obj_in)
        await session.commit()
        await session.refresh(obj_in)

        return obj_in


donation_transactions = Transactions(Donation)
project_transactions = Transactions(CharityProject)
