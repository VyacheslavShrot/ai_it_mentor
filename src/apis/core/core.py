import json

from fastapi import APIRouter, File, UploadFile, Form
from kafka import KafkaProducer

from apis.core.kafka_conf import CoreApiConsumer
from apis.core.models import Body


class CoreApis(CoreApiConsumer):
    def __init__(self):
        super().__init__()

        self.router = APIRouter()
        self.router.add_api_route("/create/response", self.create_response, methods=["POST"])
        self.router.add_api_route("/continue/create/response", self.continue_create_response, methods=["POST"])

        self.producer = KafkaProducer(bootstrap_servers=self.KAFKA_BOOTSTRAP_SERVERS)
        self.topic = "core-api"

    async def create_response(self, body: Body):
        try:
            self.logger.info("\n----Start Creating Response----\n")

            user_input_prompt = body.text
            path = body.path

            create_response_data = {
                "user_input_prompt": user_input_prompt,
                "path": path
            }
            self.producer.send(
                self.topic,
                key=b"create_response",
                value=json.dumps(
                    create_response_data
                ).encode()
            )
            self.logger.info("\n----Success Send Job to Kafka----\n")
            return {
                "success": True
            }
        except Exception as e:
            self.logger.error(
                f"\n----Unexpected error while creating and saving response----\n | {e}\n"
            )
            return {
                "error": f"Unexpected error while creating and saving response | {e}"
            }

    async def continue_create_response(
            self,
            file: UploadFile = File(...),
            text: str = Form(...),
            path: str = Form(...)
    ):
        try:
            self.logger.info("\n----Start Continue Creating Response----\n")
            if not file.filename.endswith(".txt"):
                return {
                    "error": "File should be in txt mode with .txt extension"
                }
            roadmap = await file.read()
            roadmap_text = roadmap.decode()

            continue_create_response_data = {
                "roadmap": roadmap_text,
                "continue_user_input_prompt": text,
                "path": path
            }
            self.producer.send(
                self.topic,
                key=b"continue_create_response",
                value=json.dumps(
                    continue_create_response_data
                ).encode()
            )
            self.logger.info("\n----Success Send Job to Kafka----\n")
            return {
                "success": True
            }
        except Exception as e:
            self.logger.error(
                f"\n----Unexpected error while continue creating and saving response----\n | {e}\n"
            )
            return {
                "error": f"Unexpected error while continue creating and saving response | {e}"
            }
