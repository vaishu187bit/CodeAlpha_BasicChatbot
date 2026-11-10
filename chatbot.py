"""
CodeAlpha Internship - Task 4: Basic Chatbot
Student Name: Akshita singh
Student ID: CA/DF1/316239
Domain: Python Programming

Key Concepts Used:
- if-elif: for rule-based intent matching and keyword routing
- functions: modular responses, greeting generation, and sanitization
- loops: while loop to keep the conversation going until user exits
- input/output: interactive terminal conversation interface
"""

import sys
from datetime import datetime


def get_greeting():
    """Return a time-appropriate greeting."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def chatbot_response(user_input):
    """
    Generate responses based on predefined rule matching as per Task 4 scope.
    Handles 'hello', 'how are you', 'bye', and other interactive queries.
    """
    clean_input = user_input.strip().lower()

    if not clean_input:
        return "Please say something! I'm here to chat."

    # Exit intent
    if clean_input in ["bye", "exit", "quit", "goodbye", "see you"]:
        return "Goodbye! Have a wonderful day ahead!"

    # Greetings
    elif any(greeting in clean_input for greeting in ["hello", "hi", "hey", "greetings"]):
        return f"Hi there! {get_greeting()}! How can I help you today?"

    # Well-being questions
    elif "how are you" in clean_input or "how are you doing" in clean_input or "how's it going" in clean_input:
        return "I'm fine, thanks! Everything is running smoothly. How are you doing?"

    elif "i am good" in clean_input or "i'm good" in clean_input or "i am fine" in clean_input or "great" in clean_input:
        return "That's wonderful to hear! What would you like to talk about?"

    # Name and identity
    elif "what is your name" in clean_input or "who are you" in clean_input:
        return "I am AlphaBot, a rule-based virtual assistant created for the CodeAlpha Python Internship!"

    # Time queries
    elif "time" in clean_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # Date queries
    elif "date" in clean_input or "day" in clean_input:
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}."

    # Help
    elif "help" in clean_input:
        return "You can greet me (say 'hello'), ask how I am ('how are you'), ask for the 'time' or 'date', or type 'bye' to exit."

    # Default fallback response
    else:
        return "I'm not sure I understand that yet, but I'm learning! Type 'help' to see what you can ask me."


def start_chat():
    """Run the interactive chatbot loop."""
    print("=" * 60)
    print("           WELCOME TO CODEALPHA BASIC CHATBOT")
    print("=" * 60)
    print("AlphaBot: Hello! I am your CodeAlpha Assistant.")
    print("          Type 'bye' or 'exit' whenever you want to leave.")
    print("-" * 60)

    while True:
        try:
            user_message = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAlphaBot: Goodbye! Have a great day!")
            break

        reply = chatbot_response(user_message)
        print(f"AlphaBot: {reply}")

        if user_message.lower() in ["bye", "exit", "quit", "goodbye", "see you"]:
            break


if __name__ == "__main__":
    start_chat()
