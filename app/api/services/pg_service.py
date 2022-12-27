import uuid
from datetime import datetime

import psycopg
from api.models import Review
from api.settings import settings
from psycopg.rows import dict_row


class PgService:

    now = datetime.now()

    async def _fetch_async(self, sql, *args) -> dict:
        async with await psycopg.AsyncConnection.connect(settings.pg_conn_str) as aconn:
            async with aconn.cursor(row_factory=dict_row) as acur:
                await acur.execute(sql, (*args,))
                result = await acur.fetchone()
                return result

    async def _insert_async(self, sql, *args) -> None:
        async with await psycopg.AsyncConnection.connect(settings.pg_conn_str) as aconn:
            async with aconn.cursor(row_factory=dict_row) as acur:
                await acur.execute(sql, (*args,))
                await aconn.commit()

    async def get_review(self, review_id: int) -> int:
        sql = """SELECT * FROM reviews r JOIN meta m on r.id = m.review_id where m.review_id = %s"""
        review = await self._fetch_async(sql, review_id)
        review_obj = Review(**review)
        likes = await self.get_review_likes(review_id)
        review_obj.likes = likes["count"]
        return review_obj

    async def get_review_likes(self, review_id: int) -> int:
        sql = """SELECT COUNT(*) FROM reviews_likes WHERE review_id = %s"""
        likes = await self._fetch_async(sql, review_id)
        return likes

    async def like_review(self, review_id: int):
        sql = """INSERT INTO reviews_likes (user_id, review_id, date) VALUES (%s, %s, %s)"""
        user_id = str(uuid.uuid4())
        date = self.now
        await self._insert_async(sql, user_id, review_id, date)
