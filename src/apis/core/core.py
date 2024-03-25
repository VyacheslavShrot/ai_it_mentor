import json

from fastapi import APIRouter
from kafka import KafkaProducer

from apis.core.kafka_conf import CoreApiConsumer
from apis.core.models import Body


class CoreApis(CoreApiConsumer):
    def __init__(self):
        super().__init__()
        self.router = APIRouter()
        self.router.add_api_route("/create/response", self.create_response, methods=["POST"])

    async def create_response(self, body: Body):
        try:

            self.logger.info("\n----Start Creating Response----\n")
            producer = KafkaProducer(bootstrap_servers=self.KAFKA_BOOTSTRAP_SERVERS)
            topic = "core-api"

            user_input_prompt = body.text
            path = body.path

            create_response_data = {
                "user_input_prompt": user_input_prompt,
                "path": path
            }
            producer.send(
                topic,
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
