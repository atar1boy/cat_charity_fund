from sqlalchemy import Column, String, Text

from app.models import ProjectAndDonationBaseModel


class CharityProject(ProjectAndDonationBaseModel):
    """
    Модель благотворительный проект.
    """

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        repr_data = {
            'Название проекта': self.name,
            'Описание проекта': self.description
        }
        return super().__repr__(repr_data)
