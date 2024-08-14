## My Robo Friend - A Simple Chatbot

This is a basic chatbot application built using Python's Tkinter library. It provides a simple chat interface where users can type messages and receive responses from the bot.

Right now, it's learning to be polite: it can say hello back to you in different ways.

### Features

- **Keyword-based Responses:** The chatbot uses a rule-based approach to identify keywords in user inputs and generate pre-defined responses.
- **Greeting Recognition:** It can recognize various greetings like "hi," "hello," "namaste," and respond accordingly.
- **Limited Conversation:** The bot can handle a few basic queries beyond greetings, like "how are you?" or questions about its name.
- **Simple GUI:** The application uses Tkinter to create a user-friendly interface with input and output text areas.

### How to Run

_Prerequisites:_

Python 3.x installed on your system.

Poetry installed globally: https://python-poetry.org/docs/

1. **After cloning, navigate to the project directory:**

   ```bash
   cd chat_bot
   ```

2. **Install dependencies:**

   Poetry manages dependencies in a virtual environment automatically. Run the following commands to activate virtualenv and install all required packages:

   ```bash
      poetry shell
      poetry install
   ```

3. **Run the chatbot:**
   ```bash
   # to execute the script withing the environment
   poetry run python main.py
   ```

Ask 'how are you?' or ask for it's name!

### Customization

You can easily customize the chatbot's responses and add new keywords by modifying the `greetings` list and the conditional statements within the `get_response` function. Feel free to expand the bot's capabilities by adding more rules and interactions.
