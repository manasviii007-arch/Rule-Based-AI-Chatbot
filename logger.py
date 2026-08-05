"""
logger.py
Handles saving chatbot conversations to a log file.
"""

from datetime import datetime

LOG_FILE = "chat_history.txt"


def log_message(sender, message):
    """
    Save a single message to the chat history file.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {sender}: {message}\n")


def log_conversation(user_message, bot_message):
    """
    Save one complete interaction.
    """

    log_message("User", user_message)
    log_message("Bot", bot_message)
    file_separator()


def file_separator():
    """
    Add a separator between conversations.
    """

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write("-" * 60 + "\n")


def clear_log():
    """
    Clear the chat history.
    """

    open(LOG_FILE, "w", encoding="utf-8").close()


def view_log():
    """
    Print chat history.
    """

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print("No chat history found.")