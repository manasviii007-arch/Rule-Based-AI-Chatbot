"""
logger.py
Handles chat logging for DecodeBot.
"""

from datetime import datetime
import os

LOG_FILE = "chat_history.txt"


def create_log_file():
    """
    Creates the log file if it doesn't exist.
    """
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as file:
            file.write("=" * 60 + "\n")
            file.write("DecodeBot Chat History\n")
            file.write("=" * 60 + "\n\n")


def get_timestamp():
    """
    Returns current date and time.
    """
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


def log_message(sender, message):
    """
    Logs one message.
    """

    create_log_file()

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write(
            f"[{get_timestamp()}] {sender}: {message}\n"
        )


def log_conversation(user_message, bot_message):
    """
    Logs one complete conversation turn.
    """

    log_message("User", user_message)

    log_message("Bot", bot_message)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write("-" * 60 + "\n")


def view_log():
    """
    Prints the complete chat history.
    """

    create_log_file()

    print("\n" + "=" * 60)
    print("CHAT HISTORY")
    print("=" * 60)

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        print(file.read())

    print("=" * 60)


def clear_log():
    """
    Clears the chat history.
    """

    with open(LOG_FILE, "w", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write("DecodeBot Chat History\n")
        file.write("=" * 60 + "\n\n")

    print("Chat history cleared successfully.")