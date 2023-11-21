from sqlalchemy import Column, Text, Integer, ForeignKey

from app.core.db import AbstractModel


class Donation(AbstractModel):
    """
    Модель пожертвований.
    """

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = Column(Text)
