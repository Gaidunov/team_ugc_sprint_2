import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_port: int = os.environ["mongo_port"]
    pg_conn_str: str = os.environ["pg_conn_str"]
    mongo_conn_str: str = os.environ["mongo_conn_str"]


settings = Settings()
