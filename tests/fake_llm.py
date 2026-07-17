from llm.base import BaseLLM
from llm.response import LLMResponse


class FakeLLM(BaseLLM):

    def generate(self, conversation):

        return LLMResponse(
            "Hello from Fake LLM!"
        )