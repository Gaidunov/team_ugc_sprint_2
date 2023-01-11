import psycopg2
from psycopg2 import extras
from psycopg2.extras import RealDictCursor

from data_load.models import Review
from data_load.settings import settings

conn = psycopg2.connect(
    user=settings.pg_user,
    password=settings.pg_password,
    host=settings.pg_host,
    port=settings.pg_port,
    database=settings.pg_db,
)
cur = conn.cursor(cursor_factory=RealDictCursor)


def pg_upload_review_data(data: list):

    review_sql = """
        INSERT INTO reviews (id, text, movie_id) 
        VALUES (%s, %s, %s);
    """

    meta_sql = """
            INSERT INTO meta (author_id, author_name,
            date, review_id) 
            VALUES (%s, %s, %s, %s);
    """

    review_data = tuple(
        (
            rev["review_id"],
            rev["text"],
            rev["movie_id"],
        )
        for rev in data
    )
    meta_data = tuple(
        (
            (rev["author_id"],),
            rev["author_name"],
            rev["date"],
            rev["review_id"]
        )
        for rev in data
    )
    try:
        extras.execute_batch(cur, review_sql, review_data, page_size=10)
        extras.execute_batch(cur, meta_sql, meta_data, page_size=10)
    except psycopg2.errors.UniqueViolation:
        print("\nтакое уже есть в БД", review_data[0][0])
    conn.commit()


def pg_select_review(review_id) -> dict:
    sql = """SELECT * FROM reviews r JOIN meta m 
    on r.id = m.review_id where m.review_id = %s"""
    cur.execute(sql, (review_id,))
    review = cur.fetchone()
    review = Review(**review)
    return review


def upload_review_likes(data: list) -> None:
    sql = """INSERT INTO reviews_likes 
    (user_id, review_id, date) VALUES (%s, %s, %s)"""
    like_data = (
        (str(e["user_id"]), e["review_id"], e["date"])
        for e in data
    )
    try:
        extras.execute_batch(cur, sql, like_data, page_size=10)
    except psycopg2.errors.UniqueViolation:
        print("\nтакое уже есть в БД", like_data[0][0])
    conn.commit()


def get_review_likes(review_id) -> int:
    sql = """SELECT COUNT(*) FROM reviews_likes 
    WHERE review_id = %s"""
    cur.execute(sql, (review_id,))
    likes = cur.fetchone()
    return likes
