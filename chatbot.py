from tkinter import *
from tkinter import scrolledtext


def send_text():
    # Get the text input from the 'input_text' field
    user_input = input_text.get("1.0", END).strip()
    # Enable editing of the 'display_text' field
    display_text.config(state=NORMAL)
    # Show the user's input in the 'display_text' field
    display_text.insert(END, "You: " + user_input + "\n", "user")
    user_input = user_input.lower()

    # Generate bot response by checking for keywords in user's input
    if any(x in user_input for x in greetings):
        display_text.insert(END, "Bot: Hi! What's up?\n", "bot")
    elif "how are you" in user_input:
        display_text.insert(END, "Bot: I'm just a bot!\n", "bot")
    elif "do you have a name" or "what is your name" in user_input:
        display_text.insert(END, "Bot: I don't have one. Give me a name!\n", "bot")
    else:
        display_text.insert(END, "Bot: I'm not sure how to reply...\n", "bot")

    # Clear the input field
    input_text.delete("1.0", END)
    # Disable editing of the 'display_text' field
    display_text.config(state=DISABLED)


# Create the main application window
root = Tk()
root.title("My Robo Friend")
root.geometry("500x600")

# Create a label for the application's header
app_header = Label(
    root, text="My Robo Friend", bg="Pink", fg="White", font=("Helvetica", 24)
)
app_header.pack(fill=X, expand=True)

# Create scrolled text for displaying conversation
display_text = scrolledtext.ScrolledText(root, state=DISABLED, wrap=WORD)
display_text.pack(fill=BOTH, expand=True)

# Configure text tags for styling user and bot messages
display_text.tag_config("user", foreground="Dark Blue")
display_text.tag_config("bot", foreground="Dark Green")

# Create a scrolled text field for user input
input_text = scrolledtext.ScrolledText(root, wrap=WORD, height=3)
input_text.pack(fill=BOTH, expand=True)

# Create a button for sending user input
send_button = Button(root, text="Send", font=("Helvetica,10"), command=send_text)
send_button.pack()

# Define key words for greetings
greetings = ["hi", "hello", "namaste", "hey", "howdy", "whatsup", "hola"]


# Start the main application loop
root.mainloop()
