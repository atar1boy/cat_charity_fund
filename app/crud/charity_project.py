from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    # async def get_not_closed_projects(
    #         self,
    #         session: AsyncSession,
    # ) -> List[CharityProject]:
    #     projects = await session.execute(
    #         select(CharityProject).where(
    #             CharityProject.fully_invested == 'False').order_by(
    #                 CharityProject.create_date)
    #     )
    #     projects = projects.scalars().all()
    #     return projects


charity_project_crud = CRUDCharityProject(CharityProject)
