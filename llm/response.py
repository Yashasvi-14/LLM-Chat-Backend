from dataclasses import dataclass

@dataclass
class LLMResponse:

    def __init__(self, text: str):
        self.text = text