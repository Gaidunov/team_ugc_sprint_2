from locust import HttpUser, task, between, constant, tag
from random import randint 


class MoviewApiTest(HttpUser):
    wait_time = between(0.2, 1)
    host = 'http://127.0.0.1:5000'

    @tag('mongo')
    @task
    def get_reviews_mongo(self):
        id_ = randint(1, 500000)
        self.client.get(f"/reviews/mongo/{id_}", name='mongo_test')

    @tag('postgres')
    @task
    def get_reviews_postgres(self):
        id_ = randint(1, 500000)
        self.client.get(f"/reviews/postgres/{id_}", name='postgres_test')

    @tag('like_postgres')
    @task
    def like_review_pg(self):
        id_ = randint(1, 500000)
        self.client.post(f"/reviews/postgres/like/{id_}", name='postgres_test')

    @tag('like_mongo')
    @task
    def like_review_mongo(self):
        id_ = randint(1, 500000)
        self.client.post(f"/reviews/mongo/like/{id_}", name='mongo_test')