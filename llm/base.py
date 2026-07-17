from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def generate(self, conversation):
        """Generate a response for the given conversation."""
        pass