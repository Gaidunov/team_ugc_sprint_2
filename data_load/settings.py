from pydantic import BaseSettings

class Settings(BaseSettings):
    pg_port:int
    pg_db:str
    pg_host:str='localhost'
    pg_user:str
    pg_password:str 
    mongo_port:int

    class Config:
        env_file = '.env'

settings = Settings()

