"""
chatbot.py
Main file for DecodeBot v2.0
"""

from responses import RESPONSES
from utils import *

# ==============================
# Banner
# ==============================

clear_screen()
banner()

# ==============================
# User Information
# ==============================

history = []

name = input("\nBot : Hello! What's your name?\nYou : ").strip()

if name == "":
    name = "Friend"

bot_print(f"Nice to meet you, {name}!")
bot_print("Type 'help' to view all available commands.")

# ==============================
# Chat Loop
# ==============================

while True:

    user = input(f"\n{name} : ").lower().strip()

    history.append(f"{name}: {user}")

    # ==========================
    # EXIT
    # ==========================

    if user in ["exit", "bye", "quit"]:

        reply = RESPONSES.get(user)

        bot_print(reply)

        history.append(f"Bot: {reply}")

        save_chat(user, reply)

        print("\nConversation saved to chat_history.txt")

        break

    # ==========================
    # HELP
    # ==========================

    elif user == "help":

        show_help()

        history.append("Bot: Displayed Help Menu")

    # ==========================
    # CALCULATOR
    # ==========================

    elif user == "calculator":

        calculator()

        history.append("Bot: Calculator Used")

    # ==========================
    # SQUARE
    # ==========================

    elif user == "square":

        square()

        history.append("Bot: Square Calculated")

    # ==========================
    # CUBE
    # ==========================

    elif user == "cube":

        cube()

        history.append("Bot: Cube Calculated")

    # ==========================
    # FACTORIAL
    # ==========================

    elif user == "factorial":

        factorial()

        history.append("Bot: Factorial Calculated")

    # ==========================
    # PERCENTAGE
    # ==========================

    elif user == "percentage":

        percentage()

        history.append("Bot: Percentage Calculated")

    # ==========================
    # TABLE
    # ==========================

    elif user == "table":

        table()

        history.append("Bot: Multiplication Table Generated")

    # ==========================
    # JOKE
    # ==========================

    elif user == "joke":

        tell_joke()

        history.append("Bot: Told a Joke")

    # ==========================
    # FACT
    # ==========================

    elif user == "fact":

        tell_fact()

        history.append("Bot: Shared a Fact")

    # ==========================
    # MOTIVATION
    # ==========================

    elif user == "motivate":

        motivate()

        history.append("Bot: Motivation Quote")

    # ==========================
    # DATE
    # ==========================

    elif user == "date":

        show_date()

        history.append("Bot: Displayed Date")

    # ==========================
    # TIME
    # ==========================

    elif user == "time":

        show_time()

        history.append("Bot: Displayed Time")

    # ==========================
    # SYSTEM
    # ==========================

    elif user == "system":

        system_info()

        history.append("Bot: Displayed System Information")

    # ==========================
    # QUIZ
    # ==========================

    elif user == "quiz":

        quiz()

        history.append("Bot: Quiz Completed")

    # ==========================
    # HISTORY
    # ==========================

    elif user == "history":

        show_history(history)

    # ==========================
    # CLEAR
    # ==========================

    elif user == "clear":

        clear_screen()

        banner()

    # ==========================
    # ABOUT
    # ==========================

    elif user == "about":

        reply = RESPONSES.get("about")

        bot_print(reply)

        history.append(f"Bot: {reply}")

        save_chat(user, reply)

    # ==========================
    # PREDEFINED RESPONSES
    # ==========================

    else:

        reply = RESPONSES.get(user)

        if reply:

            bot_print(reply)

            history.append(f"Bot: {reply}")

            save_chat(user, reply)

        else:

            unknown = (
                "Sorry, I don't understand that command.\n"
                "Type 'help' to see all available commands."
            )

            bot_print(unknown)

            history.append("Bot: Unknown Command")

            save_chat(user, unknown)

print("\nThank you for using DecodeBot!")
print("See you again soon!")