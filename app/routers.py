from fastapi import APIRouter, status

weater_router = APIRouter()


@weater_router.get("/", status_code=status.HTTP_200_OK)
async def get_index():
    return {"message": "Hello, sweety"}
