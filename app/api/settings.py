from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_port: int
    pg_conn_str: str
    mongo_conn_str: str

    class Config:
        env_file = ".env"


settings = Settings()
