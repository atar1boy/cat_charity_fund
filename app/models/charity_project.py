from sqlalchemy import Column, String, Text

from app.core.db import AbstractModel


class CharityProject(AbstractModel):
    """
    Модель благотворительный проект.
    """

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
