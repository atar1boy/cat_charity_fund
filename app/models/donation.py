from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models import ProjectAndDonationBaseModel


class Donation(ProjectAndDonationBaseModel):
    """
    Модель пожертвований.
    """

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = Column(Text)

    def __repr__(self):
        repr_data = {
            'id пользователя': {self.user_id},
            'Комментарий': {self.comment}
        }
        return super().__repr__(repr_data)
