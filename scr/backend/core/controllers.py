from abc import ABC
from typing import Any

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


class ControllerBase(ABC):
    model: Any

    @classmethod
    async def get(cls, item_id: int, session: AsyncSession = None):
        statement = select(cls.model).where(cls.model.id == item_id)
        result = await session.execute(statement)
        return result.scalar_one_or_none()

    @classmethod
    async def get_items(cls, page: int = 1, limit: int = 100,
                        session: AsyncSession = None):
        offset = max(page - 1, 0) * limit
        statement = select(cls.model).offset(offset).limit(limit).order_by(
            cls.model.id)
        result = await session.execute(statement)
        return result.scalars().all()

    @classmethod
    async def create(cls, partner: dict, session: AsyncSession = None):
        ...

    @classmethod
    async def update(cls, partner: dict, session: AsyncSession = None):
        ...

    @classmethod
    async def delete(cls, item_id: int, session: AsyncSession = None):
        ...
