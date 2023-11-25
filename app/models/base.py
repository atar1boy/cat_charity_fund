from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, DateTime, CheckConstraint

from app.core.db import Base


class ProjectAndDonationBaseModel(Base):
    """
    Родительский класс для моделей CharityProject и Donation.
    """
    __abstract__ = True
    __table_args__ = (
        CheckConstraint('full_amount > fully_invested'),
        CheckConstraint('fully_invested >= 0'),
    )

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)

    def __repr__(self, repr_data: dict = None):
        representation = (
            f'Модель: {self.__class__.__name__}, '
            f'Полная сумма: {self.full_amount}, '
            f'Дата создания: {self.create_date}, '
        )
        if repr_data is None:
            return representation

        for key in repr_data.keys():
            representation += f'{key}: {repr_data[key]}, '

        return representation
