import uuid
from datetime import datetime

from api.models import Review
from api.settings import settings
from motor.motor_asyncio import AsyncIOMotorClient


class MongoService:
    async def connect_to_database(self):
        self.client = AsyncIOMotorClient(
            settings.mongo_conn_str, maxPoolSize=100, minPoolSize=10
        )
        self.db = self.client.movies
        self.likes = self.db.likes
        self.reviews = self.db.reviews

    async def get_review_likes(self, review_id: int = 100) -> int:
        like_count = await self.db.likes.count_documents({"review_id": review_id})
        return like_count

    async def get_review(self, review_id: int = 123) -> Review:
        review = await self.reviews.find_one({"review_id": review_id})
        review_obj = Review(**review)
        review_obj.likes = await self.get_review_likes(review_id)
        self.client.close()
        return review_obj

    async def like_review(self, review_id: int):
        user_id = str(uuid.uuid4())
        now = datetime.now()
        await self.likes.insert_one(
            {"review_id": review_id, "user_id": user_id, "date": now}
        )
