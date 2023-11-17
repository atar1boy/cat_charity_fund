from sqlalchemy import Column, String

from app.core.db import Base


class CharityProject(Base):
    """
    Модель благотворительный проект.
    """
    name = Column(String(100), unique=True, nullable=False)
