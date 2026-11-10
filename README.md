# CodeAlpha_BasicChatbot

A rule-based virtual conversational assistant built in Python for the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
- **Student Name:** Akshita singh
- **Student ID:** CA/DF1/316239
- **Domain:** Python Programming
- **Batch:** 10th October 2026 to 10th November 2026
- **Task 4:** Basic Chatbot

---

## 🎯 Goal & Specifications
The goal is to develop a simple rule-based chatbot capable of handling conversational user inputs with predefined responses.

### Scope Covered:
- **Greetings:** Responds to user inputs like `"hello"`, `"hi"`, `"hey"` with personalized and time-aware replies.
- **Well-Being Questions:** Responds to `"how are you"` with predefined replies like `"I'm fine, thanks!"`.
- **Exit & Goodbye:** Accurately identifies exit triggers like `"bye"`, `"quit"`, or `"exit"` and bids farewell (`"Goodbye!"`).
- **Additional Capabilities:** Reports the current live time and date, introduces itself, and offers a helpful fallback for unrecognized prompts.

---

## 🧠 Key Concepts Used
- **`if-elif` Statements:** Evaluates input queries and directs the logic to the appropriate response branch.
- **Functions:** Modular design for formatting, time detection, and response generation.
- **Loops (`while` loop):** Keeps the interactive conversation active until an exit command is provided.
- **Input/Output (`input()`, `print()`):** Clean, formatted console interaction.

---

## 🚀 How to Run

### Prerequisites
- Python 3.8+ or `uv` installed.

### Running the Chatbot
Open your terminal in this directory and execute:

```bash
python chatbot.py
```
*(Or if using uv)*:
```bash
uv run python chatbot.py
```

### Running Tests
To run the automated test suite:
```bash
python -m unittest test_chatbot.py
```

---

## 💬 Sample Interaction
```text
============================================================
           WELCOME TO CODEALPHA BASIC CHATBOT
============================================================
AlphaBot: Hello! I am your CodeAlpha Assistant.
          Type 'bye' or 'exit' whenever you want to leave.
------------------------------------------------------------

You: hello
AlphaBot: Hi there! Good evening! How can I help you today?

You: how are you
AlphaBot: I'm fine, thanks! Everything is running smoothly. How are you doing?

You: what is your name
AlphaBot: I am AlphaBot, a rule-based virtual assistant created for the CodeAlpha Python Internship!

You: bye
AlphaBot: Goodbye! Have a wonderful day ahead!
```

---

## 📄 License
This project is licensed under the MIT License.
