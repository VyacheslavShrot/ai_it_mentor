import logging

from environs import Env
from fastapi import FastAPI

from apis.core import core_router

env = Env()
env.read_env('.env')

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI IT Mentor"
)


@app.get("/app-status")
async def app_status():
    return {"status": "success"}

app.include_router(core_router)
