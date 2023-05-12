from abc import ABC

from fastapi import APIRouter, Header, Query, Body, Path, Depends
from fastapi.responses import JSONResponse
from sqlmodel.ext.asyncio.session import AsyncSession

from scr.backend.app.db import get_session
from scr.backend.core.controllers import ControllerBase


class RouterBase(ABC):
    controller: ControllerBase
    tags: list[str] = []
    path: str = ''
    path_plural: str = ''
    router: APIRouter

    def __init__(self):
        self.router = APIRouter(tags=self.tags)
        self.router.add_api_route(
            f'/{self.path}',
            self.create_item,
            methods=['POST'],
            summary='Create new item',
            description='Создает новую запись',
            response_model=self.controller.model,
        )
        self.router.add_api_route(
            f'/{self.path_plural}',
            self.get_items,
            methods=['GET'],
            summary='Get items',
            description='Возвращает коллекцию записей',
            # response_model=list[self.controller.model],
        )
        self.router.add_api_route(
            f'/{self.path}/{{item_id}}',
            self.get_item,
            methods=['GET'],
            summary='Get item by ID',
            description='Возвращает запись по идентификатору',
            response_model=self.controller.model,
        )
        self.router.add_api_route(
            f'/{self.path}/{{item_id}}',
            self.update_item,
            methods=['PATCH'],
            summary='Update item by ID',
            description='Обновляет запись по идентификатору',
            response_model=self.controller.model,
        )
        self.router.add_api_route(
            f'/{self.path}/{{item_id}}',
            self.delete_item,
            methods=['DELETE'],
            summary='Delete item by ID',
            description='Удаляет запись по идентификатору',
        )

    @classmethod
    async def create_item(
            cls=Header(include_in_schema=False),
            item_data: dict = Body(),
            session: AsyncSession = Depends(get_session)
    ):
        if item_data is None:
            item_data = {}
        result = await cls.controller.create(item_data, session)
        return result

    @classmethod
    async def get_items(
            cls=Header(include_in_schema=False),
            page: int = Query(1),
            limit: int = Query(100),
            session: AsyncSession = Depends(get_session)
    ):
        result = await cls.controller.get_items(page, limit, session)
        if result is None:
            return JSONResponse('Item not found', status_code=404)
        return result

    @classmethod
    async def get_item(
            cls=Header(include_in_schema=False),
            item_id: int = Path(),
            session: AsyncSession = Depends(get_session)
    ):
        result = await cls.controller.get(item_id, session)
        if result is None:
            return JSONResponse('Item not found', status_code=404)
        return result

    @classmethod
    async def update_item(
            cls=Header(include_in_schema=False),
            item_data: dict = Body(),
            session: AsyncSession = Depends(get_session)
    ):
        result = await cls.controller.update(item_data, session)
        return result

    @classmethod
    async def delete_item(
            cls=Header(include_in_schema=False),
            item_id: int = Path(),
            session: AsyncSession = Depends(get_session)
    ):
        result = await cls.controller.delete(item_id, session)
        return result
