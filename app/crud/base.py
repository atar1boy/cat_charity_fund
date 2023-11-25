from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:
    """
    Базовые CRUD функции проекта.
    """

    def __init__(self, model):
        self.model = model

    async def get(
            self,
            obj_id: int,
            session: AsyncSession,
    ):
        """Получить объект из базы данных."""
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )
        return db_obj.scalars().first()

    async def get_multi(
            self,
            session: AsyncSession
    ):
        """Получить объекты из базы данных."""
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
            self,
            obj_in,
            session: AsyncSession,
            without_commit=False
    ):
        """Создать объект в базе данных."""
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        if without_commit:
            return db_obj
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def user_create(
        self,
        obj_in,
        session: AsyncSession,
        user_id: int,
        without_commit=False
    ):
        obj_in_data = obj_in.dict()
        obj_in_data['user_id'] = user_id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        if without_commit:
            return db_obj
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSession,
    ):
        """Изменить объект в базе данных."""
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
            self,
            db_obj,
            session: AsyncSession,
    ):
        """Удалить объект в базе данных."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_not_closed_objs(
            self,
            session: AsyncSession,
    ):
        objs = await session.execute(
            select(self.model).where(
                self.model.fully_invested == False).order_by(desc(  # noqa
                    (self.model.id)))  # noqa. Нужно заменить на 'self.model.create_data', сортировка по id использована как костыль для тестов.
        )
        objs = objs.scalars().all()
        return objs
