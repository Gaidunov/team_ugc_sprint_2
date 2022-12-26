from pymongo import MongoClient

from data_load.settings import settings

client = MongoClient(port=int(settings.mongo_port))   
db = client.movies
review_collection = db.reviews
likes_collection = db.likes

def mongo_upload_reviews(data:list):
    review_collection.insert_many(data)

def mongo_upload_likes(data:list):
    likes_collection.insert_many(data)

def mongo_select(review_id):
    review = review_collection.find_one({"review_id":review_id})
    return review

def get_review_likes(review_id:int)->int:
    like_count = likes_collection.count_documents({"review_id":review_id})
    return like_count
