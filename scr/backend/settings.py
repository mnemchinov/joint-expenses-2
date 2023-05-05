from os import environ

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Совместные покупки'
    debug: bool = True
    version: str = '0.0.1'
    description: str = 'Минисервис для учета совместных закупок'

    db_user: str = environ.get('DB_USER')
    db_password: str = environ.get('DB_PASSWORD')
    db_name: str = environ.get('DB_NAME')
    db_host: str = environ.get('DB_HOST')
    db_port: str = environ.get('DB_PORT')
    db_url: str = f'postgresql+asyncpg://' \
                  f'{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    db_echo: bool = True
    db_pool_size: int = 10
    db_pool_recycle: int = 3600
    db_max_overflow: int = 20
    db_pool_pre_ping: bool = True
    db_query_cache_size: int = 65536  # statement cache size


settings = Settings()
