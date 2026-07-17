import json
import os
class Conversation:

    def __init__(self):
        self.messages: list[dict] = []

    def add_message(self, role, content) -> None:
        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )

    def get_messages(self) -> list:
        return self.messages
    
    def save_to_file(self, filename: str) -> None:

        with open(filename, "w") as file:
            json.dump(self.messages, file, indent=4)
    
    def load_from_file(self, filename: str) -> None:

        if not os.path.exists(filename):
            self.messages = []
            return

        with open(filename, "r") as file:
            self.messages = json.load(file)