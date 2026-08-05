"""
chatbot.py
DecodeBot v2.0
Main Application
"""

from responses import (
    RESPONSES,
    GREETING_COMMANDS,
    EXIT_COMMANDS,
    random_greeting,
    random_joke,
    random_fact,
    random_quote
)

from utils import (
    banner,
    bot_print,
    show_help,
    calculator,
    square,
    cube,
    factorial,
    percentage,
    table,
    show_date,
    show_time,
    system_info,
    clear_screen,
    quiz,
    show_history
)

from logger import (
    log_conversation,
    view_log
)

import os


# =====================================
# Startup
# =====================================

clear_screen()

banner()

print()

name = input("Bot : Hello! What's your name?\nYou : ").strip()

if not name:
    name = "Friend"

bot_print(f"Welcome {name}!")

bot_print("Type 'help' to view all available commands.")

history = []

print()

# =====================================
# Main Chat Loop
# =====================================

while True:

    user = input(f"{name} : ").lower().strip()

    history.append(f"{name}: {user}")

    # =====================================
    # Greeting Commands
    # =====================================

    if user in GREETING_COMMANDS:

        reply = random_greeting()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue


    # =====================================
    # Exit Commands
    # =====================================

    elif user in EXIT_COMMANDS:

        reply = RESPONSES[user]

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        print("\nConversation saved successfully.")

        break


    # =====================================
    # Help
    # =====================================

    elif user == "help":

        show_help()

        history.append("Bot: Displayed help menu")

        continue


    # =====================================
    # Calculator
    # =====================================

    elif user == "calculator":

        calculator()

        history.append("Bot: Calculator opened")

        continue


    # =====================================
    # Square
    # =====================================

    elif user == "square":

        square()

        history.append("Bot: Square calculated")

        continue


    # =====================================
    # Cube
    # =====================================

    elif user == "cube":

        cube()

        history.append("Bot: Cube calculated")

        continue


    # =====================================
    # Factorial
    # =====================================

    elif user == "factorial":

        factorial()

        history.append("Bot: Factorial calculated")

        continue


    # =====================================
    # Percentage
    # =====================================

    elif user == "percentage":

        percentage()

        history.append("Bot: Percentage calculated")

        continue


    # =====================================
    # Multiplication Table
    # =====================================

    elif user == "table":

        table()

        history.append("Bot: Table generated")

        continue


    # =====================================
    # Joke
    # =====================================

    elif user == "joke":

        reply = random_joke()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue


    # =====================================
    # Fact
    # =====================================

    elif user == "fact":

        reply = random_fact()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue


    # =====================================
    # Motivation
    # =====================================

    elif user == "motivate":

        reply = random_quote()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue


    # =====================================
    # Date
    # =====================================

    elif user == "date":

        show_date()

        history.append("Bot: Displayed current date")

        continue


    # =====================================
    # Time
    # =====================================

    elif user == "time":

        show_time()

        history.append("Bot: Displayed current time")

        continue
    # =====================================
    # System Information
    # =====================================

    elif user == "system":

        system_info()

        history.append("Bot: Displayed system information")

        continue


    # =====================================
    # Quiz
    # =====================================

    elif user == "quiz":

        quiz()

        history.append("Bot: Quiz completed")

        continue


    # =====================================
    # History
    # =====================================

    elif user == "history":

        show_history(history)

        history.append("Bot: Displayed conversation history")

        continue


    # =====================================
    # Log File
    # =====================================

    elif user == "logs":

        print()

        view_log()

        print()

        continue


    # =====================================
    # Clear Screen
    # =====================================

    elif user == "clear":

        clear_screen()

        banner()

        continue


    # =====================================
    # About Project
    # =====================================

    elif user == "about":

        reply = RESPONSES["about"]

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue


    # =====================================
    # Predefined Responses
    # =====================================

    elif user in RESPONSES:

        reply = RESPONSES[user]

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue


    # =====================================
    # Unknown Command
    # =====================================

    else:

        reply = (
            "Sorry, I couldn't understand that command.\n"
            "Type 'help' to see the list of available commands."
        )

        bot_print(reply)

        history.append("Bot: Unknown command")

        log_conversation(user, reply)

        continue


# =====================================
# Program Ends
# =====================================

print()

print("=" * 70)

print("Thank you for using DecodeBot!")

print("Hope you enjoyed exploring Rule-Based AI.")

print("Have a wonderful day!")

print("=" * 70)