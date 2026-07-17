from chatbot.chatbot import ChatBot
from llm.gemini import GeminiLLM


def main():

    llm = GeminiLLM()

    chatbot = ChatBot(llm)

    print("AI Chatbot")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:

            response = chatbot.send_message(user_input)
            print("\nAssistant:")
            print(response.text)

        except Exception as e:

            print("\nError:")
            print(e)


if __name__ == "__main__":
    main()