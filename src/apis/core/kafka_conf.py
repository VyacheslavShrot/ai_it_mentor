import json

from kafka import KafkaConsumer

from apis.core.mixins import CoreApiMixin


class CoreApiConsumer(CoreApiMixin):
    KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'

    def __init__(self):
        self.consumer = KafkaConsumer(
            'core-api',
            group_id='core-api-group',
            bootstrap_servers=[self.KAFKA_BOOTSTRAP_SERVERS],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    async def run(self):
        for message in self.consumer:
            await self.create_response(message)

    async def create_response(self, message):
        data: dict = message.value

        user_input_prompt: str = data.get("user_input_prompt", None)
        if not user_input_prompt:
            raise ValueError("'user_input_prompt' variable is None")

        path: str = data.get("path", None)
        if not user_input_prompt:
            raise ValueError("'path' variable is None")

        self.logger.info("\n----Start Creating Completion with OpenAI----\n")
        response = await self.create_completion(user_input_prompt)

        self.logger.info("\n----Start Creating Roadmap File----\n")
        await self.create_file(response, path)

        self.logger.info("\n----Success Creating Roadmap File----\n")