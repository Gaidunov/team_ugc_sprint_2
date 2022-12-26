import json
from faker import Faker
from datetime import datetime, timedelta
from random import randint, choice
import uuid

fake = Faker("ru_RU")


def get_movies_id() -> list:
    with open("data_load/movies_with_time.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return [mv[0] for mv in data]


def gen_author(id_: int) -> dict:
    name = fake.name()
    return {"author_name": name, "author_id": id_}


def gen_review_id():
    for e in range(1, 10000000):
        yield e


REVIEW_ID_GEN = gen_review_id()
MOVIE_IDS = get_movies_id()
AUTHORS = [gen_author(i) for i in range(1000)]
NUMBER_OF_REVIEWS = 500000


def make_one_review():
    text = fake.text(max_nb_chars=1000)
    author = fake.name()
    date = datetime.utcnow() - timedelta(days=randint(1, 3000))
    author = choice(AUTHORS)
    review = {
        "review_id": REVIEW_ID_GEN.__next__(),
        "text": text,
        "movie_id": choice(MOVIE_IDS),
        "author_name": author["author_name"],
        "author_id": str(author["author_id"]),
        "date": date,
    }
    return review


def make_one_user_like():
    user = str(uuid.uuid4())
    date = datetime.now() - timedelta(days=randint(1, 3000))
    like = {"user_id": user, "review_id": randint(1, NUMBER_OF_REVIEWS), "date": date}
    return like


def generate_batch(func, n=2, **kwargs):
    return [func(**kwargs) for _ in range(n)]
