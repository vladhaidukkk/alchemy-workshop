from pydantic import Field, PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str
    db_port: int = Field(ge=1, le=65535)
    db_user: str
    db_pass: str
    db_name: str

    @computed_field
    def sync_db_url(self) -> str:
        dsn = PostgresDsn.build(  # type: ignore
            scheme="postgresql+psycopg",
            host=self.db_host,
            port=self.db_port,
            username=self.db_user,
            password=self.db_pass,
            path=self.db_name,
        )
        return dsn.unicode_string()

    @computed_field
    def async_db_url(self) -> str:
        dsn = PostgresDsn.build(  # type: ignore
            scheme="postgresql+asyncpg",
            host=self.db_host,
            port=self.db_port,
            username=self.db_user,
            password=self.db_pass,
            path=self.db_name,
        )
        return dsn.unicode_string()

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()  # type: ignore
