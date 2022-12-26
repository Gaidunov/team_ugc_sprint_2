from api.services.mongo_service import MongoService
from api.services.pg_service import PgService


async def get_mongo_service()->MongoService:
    db = MongoService()
    await db.connect_to_database()
    return db

async def get_pg_service()->PgService:
    db = PgService()
    return db