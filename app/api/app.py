from api.models import Review
from api.services import get_mongo_service, get_pg_service
from fastapi import FastAPI, Depends

app = FastAPI(docs_url="/docs")


@app.get(
    "/reviews/mongo/{review_id}",
    response_model=Review,
    description="Get review from MongoDb by id.",
)
async def get_review_from_mongo(review_id: int, db=Depends(get_mongo_service)):
    """Get review by id from mongo."""
    review = await db.get_review(review_id)
    return review


@app.get(
    "/reviews/postgres/{review_id}",
    response_model=Review,
    description="Get review from Postgres by id.",
)
async def get_review_from_postgres(review_id: int, db=Depends(get_pg_service)):
    """Get review by id from postgres."""
    review = await db.get_review(review_id)
    return review


@app.post(
    "/reviews/postgres/like/{review_id}",
    description="Leave a like for a review from Postgres.",
)
async def like_pg(review_id: int, user_id: str, db=Depends(get_pg_service)):
    await db.like_review(review_id, user_id)
    return "liked"


@app.post(
    "/reviews/mongo/like/{review_id}",
    description="Leave a like for a review from MongoDb.",
)
async def like_mongo(review_id: int, user_id: str, db=Depends(get_mongo_service)):
    await db.like_review(review_id, user_id)
    return "liked"


@app.post(
    "/reviews/mongo/dislike/{review_id}",
    description="Remove like for a review from MongoDb.",
)
async def dislike_mongo(review_id: int, user_id: str, db=Depends(get_mongo_service)):
    await db.dislike_review(review_id, user_id)
    return "disliked"


@app.post(
    "/reviews/postgres/dislike/{review_id}",
    description="Remove like for a review from Postgres.",
)
async def dislike_pg(review_id: int, user_id: str, db=Depends(get_pg_service)):
    await db.dislike_review(review_id, user_id)
    return "disliked"
