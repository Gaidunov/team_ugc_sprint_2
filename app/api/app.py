from api.models import Review
from api.services import get_mongo_service, get_pg_service
from fastapi import FastAPI, Depends

app = FastAPI(docs_url="/docs")


@app.get("/reviews/mongo/{review_id}", response_model=Review)
async def get_review_from_mongo(review_id: int, db=Depends(get_mongo_service)):
    """Get review by id from mongo."""
    review = await db.get_review(review_id)
    return review


@app.get("/reviews/postgres/{review_id}", response_model=Review)
async def get_review_from_postgres(review_id: int, db=Depends(get_pg_service)):
    """Get review by id from postgres."""
    review = await db.get_review(review_id)
    return review


@app.post("/reviews/postgres/like/{review_id}")
async def like_pg(review_id: int, db=Depends(get_pg_service)):
    await db.like_review(review_id)
    return "liked"


@app.post("/reviews/mongo/like/{review_id}")
async def like_mongo(review_id: int, db=Depends(get_mongo_service)):
    await db.like_review(review_id)
    return "liked"
