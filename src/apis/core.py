from fastapi import APIRouter

core_router = APIRouter()


@core_router.post("/create/response")
def create_response():
    ...
