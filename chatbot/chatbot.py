from chatbot.conversation import Conversation

from llm.base import BaseLLM
from llm.response import LLMResponse
from chatbot.conversation import Conversation
from utils.logger import get_logger
from config.settings import CONVERSATION_FILE
logger = get_logger(__name__)


class ChatBot:

    def __init__(self, llm: BaseLLM):

        self.llm = llm
        self.conversation = Conversation()
        self.conversation.load_from_file(
            CONVERSATION_FILE
        )

    def send_message(
        self,
        text: str
    ) -> LLMResponse:
        
        logger.info("Received user message")
        self.conversation.add_message(
            "user", text
        )

        response = self.llm.generate(
            self.conversation.get_messages()
        )
        logger.info("Successfully generated AI response")

        self.conversation.add_message(
            "assistant", response.text
        )

        self.conversation.save_to_file(
            CONVERSATION_FILE
        )

        return response


