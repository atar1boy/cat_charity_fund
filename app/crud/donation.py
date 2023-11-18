from app.crud.base import CRUDBase
from app.models.donation import Donation


class CRUDDonation(CRUDBase):
    pass


reservation_crud = CRUDDonation(Donation)
