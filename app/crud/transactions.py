from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDTransactions:

    def __init__(self, model):
        self.model = model

    async def get_not_invested_objs(
            self,
            session: AsyncSession,
    ):
        objs = await session.execute(
            select(self.model).where(
                self.model.fully_invested == False).order_by(desc(  # noqa
                    (self.model.id)))
        )
        objs = objs.scalars().all()
        return objs
