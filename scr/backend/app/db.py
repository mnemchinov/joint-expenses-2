import orjson as orjson
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from scr.backend.settings import settings

DATABASE_URL = settings.db_url

engine = create_async_engine(
    settings.db_url,
    echo=settings.db_echo,
    pool_size=settings.db_pool_size,
    pool_recycle=settings.db_pool_recycle,
    max_overflow=settings.db_max_overflow,
    pool_pre_ping=settings.db_pool_pre_ping,
    json_serializer=orjson.dumps,
    json_deserializer=orjson.loads,
    query_cache_size=settings.db_query_cache_size,
    pool_use_lifo=True,
    future=True,
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
