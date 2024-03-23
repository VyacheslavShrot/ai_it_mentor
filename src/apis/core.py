from fastapi import APIRouter


class CoreApis:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/create/response", self.create_response, methods=["POST"])

    @staticmethod
    async def create_response():
        return {"success": True}
