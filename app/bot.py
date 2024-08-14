class Chatbot:
    def __init__(self):
        self.greetings = ["hi", "hello", "namaste", "hey", "howdy", "what sup", "hola"]

    def get_response(self, user_input):
        user_input = user_input.lower()
        if any(x in user_input for x in self.greetings):
            return "Hi! What's up?\n", "bot"
        elif "how are you" in user_input:
            return "I'm just a bot!\n", "bot"
        elif "do you have a name" in user_input:
            return "I don't have one. Give me a name!\n", "bot"
        elif "what is your name" in user_input:
            return "I don't have one. Give me a name!\n", "bot"
        else:
            return "I'm not sure how to reply...\n", "bot"
