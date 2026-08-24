knowledge_base = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but I'm running smoothly! And you?",
    "what is your name": "I'm DecodeBot, a rule-based chatbot.",
    "help": "I can respond to greetings, answer simple questions, and say goodbye. Try 'hello', 'help', or 'bye'.",
    "bye": "Goodbye! Have a great day.",
    "exit": "Goodbye! Have a great day.",
}

default_response = "I'm not sure I understand. Type 'help' to see what I can do."
exit_commands = {"bye", "exit", "quit"}


def get_response(user_input: str) -> str:
    """Sanitize input and return the matched response, or a fallback."""
    sanitized_input = user_input.strip().lower()
    return knowledge_base.get(sanitized_input, default_response)


def chatbot():
    print("Chatbot: Hello! Type 'bye', 'exit', or 'quit' to end our chat.")

    while True:
        raw_input_text = input("You: ")
        user_input = raw_input_text.strip().lower()

        if not user_input:
            print("Chatbot: Please type something.")
            continue

        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input in exit_commands:
            break


if __name__ == "__main__":
    chatbot()
