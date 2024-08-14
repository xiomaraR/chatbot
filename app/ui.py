from tkinter import *
from tkinter import scrolledtext
from .bot import Chatbot


class ChatbotUI:
    def __init__(self):
        self.bot = Chatbot()
        self.root = Tk()
        self.root.title("My Robo Friend")
        self.root.geometry("500x600")

        app_header = Label(
            self.root,
            text="My Robo Friend",
            bg="Pink",
            fg="White",
            font=("Helvetica", 24),
        )
        app_header.pack(fill=X, expand=True)

        # Enable txt scrolling for displaying conversation
        self.display_text = scrolledtext.ScrolledText(
            self.root, state=DISABLED, wrap=WORD
        )
        self.display_text.pack(fill=BOTH, expand=True)

        # Configure text tags for styling user and bot messages
        self.display_text.tag_config("user", foreground="Dark Blue")
        self.display_text.tag_config("bot", foreground="Dark Green")

        # Create a scrolling text field for user input
        self.input_text = scrolledtext.ScrolledText(self.root, wrap=WORD, height=3)
        self.input_text.pack(fill=BOTH, expand=True)

        # Create a button for sending user input
        send_button = Button(
            self.root, text="Send", font=("Helvetica", 10), command=self.send_text
        )
        send_button.pack()

    def send_text(self):
        # Get the text input from the 'input_text' field
        user_input = self.input_text.get("1.0", END).strip()
        # Enable editing of the 'display_text' field
        self.display_text.config(state=NORMAL)
        # Show the user's input in the 'display_text' field
        self.display_text.insert(END, "You: " + user_input + "\n", "user")

        bot_response = self.bot.get_response(user_input)
        # Insert the response into the display_text widget
        if isinstance(bot_response, tuple):
            bot_response = bot_response[0]
        self.display_text.insert(END, f"Bot: {bot_response}\n", "bot")

        # Clear the input field
        self.input_text.delete("1.0", END)
        # Disable editing of the 'display_text' field
        self.display_text.config(state=DISABLED)


if __name__ == "__main__":
    app = ChatbotUI()
    app.root.mainloop()
