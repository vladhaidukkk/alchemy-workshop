from typing import Literal

from pydantic import BaseModel, Field, PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    host: str
    port: int = Field(ge=1, le=65535)
    username: str
    password: str | None = None
    name: str

    @computed_field
    @property
    def sync_url(self) -> str:
        dsn = PostgresDsn.build(
            scheme="postgresql+psycopg",
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            path=self.name,
        )
        return dsn.unicode_string()

    @computed_field
    @property
    def async_url(self) -> str:
        dsn = PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            path=self.name,
        )
        return dsn.unicode_string()


class AlchemySettings(BaseModel):
    echo: bool | Literal["debug"] = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10


class Settings(BaseSettings):
    debug: bool = False

    db: DatabaseSettings
    alchemy: AlchemySettings

    model_config = SettingsConfigDict(
        env_ignore_empty=True,
        env_nested_delimiter="__",
        extra="ignore",
    )


settings = Settings(_env_file=(".env.example", ".env"))
