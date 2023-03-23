from datetime import timedelta

from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn

load_dotenv()


class DataBaseSettings(BaseSettings):
    user: str = ...
    password: str = ...
    db: str = ...
    host: str = ...
    port: int = ...

    class Config:
        env_prefix = 'postgres_'


class RedisSettings(BaseSettings):
    host: str = ...
    port: int = ...

    class Config:
        env_prefix = 'redis_'


class Settings(BaseSettings):
    debug_mode: bool = False
    app_port: int = ...
    project_name: str = 'My auth service'
    project_description: str = 'Light auth microservice'

    authjwt_secret_key: str = ...
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {'access', 'refresh'}
    authjwt_access_token_expires: timedelta = timedelta(minutes=60)
    authjwt_refresh_token_expires: timedelta = timedelta(days=3)

    access_token_expires_seconds: int = authjwt_access_token_expires.total_seconds()
    refresh_token_expires_seconds: int = authjwt_refresh_token_expires.total_seconds()

    db = DataBaseSettings()
    database_dsn: PostgresDsn = f'postgresql+asyncpg://{db.user}:{db.password}@{db.host}:{db.port}/{db.db}'
    log_sql_queries: bool = False

    redis = RedisSettings()

    pagination_limit: int = 10
    grpc_port: int = ...


settings = Settings()
