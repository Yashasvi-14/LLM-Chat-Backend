import os

from dotenv import load_dotenv
from google import genai
import time
from google.genai.errors import ServerError
from config.settings import REQUEST_TIMEOUT

from llm.base import BaseLLM
from llm.response import LLMResponse
from utils.logger import get_logger
logger = get_logger(__name__)
from config.settings import MAX_RETRIES

from config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

class GeminiLLM(BaseLLM):

    def __init__(self, model=GEMINI_MODEL):
        self.model = model
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def _prepare_contents(self, conversation):
        """
        Convert our conversation format into a plain text prompt.
        """

        prompt = ""

        for message in conversation:

            role = message["role"].capitalize()
            content = message["content"]

            prompt += f"{role}: {content}\n"

        prompt += "Assistant:"

        return prompt

    def generate(self, conversation):
        
        logger.info("Preparing Gemini request.")
        contents = self._prepare_contents(conversation)
        
        for attempt in range(MAX_RETRIES):
            try:
                logger.info(
                f"Attempt {attempt + 1}/{MAX_RETRIES}"
                )

                response = self._call_model(contents)

                logger.info(
                    "Response received successfully."
                )

                return LLMResponse(response.text)

            except ServerError:
                logger.exception(
                    f"Attempt {attempt + 1} failed."
                )

                if attempt == MAX_RETRIES - 1:
                    raise
                
                delay = 2 ** attempt

                logger.warning(
                    f"Retrying in {delay} seconds..."
                )

                time.sleep(delay)
            
            except Exception:
                logger.exception(
                    "Unexpected application error."
                )
                raise
    
    def _call_model(self, contents):

        return self.client.models.generate_content(
        model=self.model,
        contents=contents
    )