import openai
from fastapi import APIRouter

from apis.core.mixins import CoreApiMixin
from apis.core.models import Body


class CoreApis(CoreApiMixin):
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/create/response", self.create_response, methods=["POST"])

    async def create_response(self, body: Body):
        user_input_prompt = body.text

        messages = [
            {
                "role": "system", "content": self.system_prompt
            },
            {
                "role": "user", "content": self.user_prompt_example
            },
            {
                "role": "assistant", "content": self.assistant_prompt_example
            },
            {
                "role": "user", "content": user_input_prompt
            }
        ]
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1.1,
            n=1
        ).choices[0].message.content
        return {
            "success": True,
            "response": response
        }
