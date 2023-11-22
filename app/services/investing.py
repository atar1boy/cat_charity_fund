from typing import Union

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject, Donation


async def investing(
        session: AsyncSession = Depends(get_async_session),
        obj_in: Union[CharityProject, Donation],
):
    ...
