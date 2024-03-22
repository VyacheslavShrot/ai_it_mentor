from fastapi import APIRouter

core_router = APIRouter()


@core_router.post("/create/response")
async def create_response():
    ...
