from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models import AbstractModel


class Donation(AbstractModel):
    """
    Модель пожертвований.
    """

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = Column(Text)
