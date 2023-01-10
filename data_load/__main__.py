import timeit
from random import randint

from tqdm import tqdm

import data_load.mongo_client as mongo_client
import data_load.pg_client as pg_client
from data_load.data_gen import (
    generate_batch,
    make_one_review,
    make_one_user_like
)


def insert_million_reviews():
    print("\nзагружаем 500 тыс. рецензий")
    for _ in tqdm(range(500)):
        data = generate_batch(make_one_review, 1000)
        pg_client.pg_upload_review_data(data)
        mongo_client.mongo_upload_reviews(data)


def insert_two_million_likes():
    print("загружаем 2 млн лайков")
    for _ in tqdm(range(200)):
        data = generate_batch(make_one_user_like, 1000)
        pg_client.upload_review_likes(data)
        mongo_client.mongo_upload_likes(data)


def measure_select():
    print(
        "postgres:",
        timeit.timeit(
            "pg_client.pg_select_review(1)",
            number=100,
            globals=globals()
        ),
    )
    print(
        "mongo:",
        timeit.timeit(
            "mongo_client.mongo_select(1)",
            number=100,
            globals=globals()
        ),
    )


def measure_likes():
    def measure_likes_count_mongo():
        for _ in tqdm(range(100)):
            review_id = randint(1, 100000)
            mongo_client.get_review_likes(review_id)

    def measure_likes_pg():
        for _ in tqdm(range(100)):
            review_id = randint(1, 100000)
            pg_client.get_review_likes(review_id)

    print(
        "mongo likes:",
        timeit.timeit(
            "measure_likes_count_mongo()",
            number=1,
            globals=locals()
        ),
    )
    print(
        "posrgres likes:",
        timeit.timeit(
            "measure_likes_pg()",
            number=1,
            globals=locals()
        ),
    )


if __name__ == "__main__":
    insert_million_reviews()
    insert_two_million_likes()
