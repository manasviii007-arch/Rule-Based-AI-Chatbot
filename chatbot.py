"""
chatbot.py
Main Application of DecodeBot v2.1
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
    show_history,
    read_knowledge,
    search_knowledge,
    about,
    goodbye
)

from logger import (
    log_conversation,
    view_log
)

from version import APP_NAME, VERSION

# ============================================
# Initial Setup
# ============================================

clear_screen()

banner()

history = []

print()

name = input("Bot : Hello! What's your name?\nYou : ").strip()

if not name:
    name = "Friend"

bot_print(f"Welcome {name}!")

bot_print(
    f"You are now using {APP_NAME} Version {VERSION}."
)

bot_print(
    "Type 'help' to see all available commands."
)

print()

# ============================================
# Main Loop
# ============================================

while True:

    user = input(f"{name} : ").lower().strip()

    history.append(f"{name}: {user}")

    # ========================================
    # Greetings
    # ========================================

    if user in GREETING_COMMANDS:

        reply = random_greeting()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue

    # ========================================
    # Exit
    # ========================================

    elif user in EXIT_COMMANDS:

        reply = RESPONSES[user]

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        goodbye()

        break

    # ========================================
    # Help
    # ========================================

    elif user == "help":

        show_help()

        history.append("Bot: Help menu shown")

        continue

    # ========================================
    # Calculator
    # ========================================

    elif user == "calculator":

        calculator()

        history.append("Bot: Calculator used")

        continue

    # ========================================
    # Square
    # ========================================

    elif user == "square":

        square()

        history.append("Bot: Square calculated")

        continue

    # ========================================
    # Cube
    # ========================================

    elif user == "cube":

        cube()

        history.append("Bot: Cube calculated")

        continue

    # ========================================
    # Factorial
    # ========================================

    elif user == "factorial":

        factorial()

        history.append("Bot: Factorial calculated")

        continue

    # ========================================
    # Percentage
    # ========================================

    elif user == "percentage":

        percentage()

        history.append("Bot: Percentage calculated")

        continue

    # ========================================
    # Multiplication Table
    # ========================================

    elif user == "table":

        table()

        history.append("Bot: Multiplication table generated")

        continue

    # ========================================
    # Joke
    # ========================================

    elif user == "joke":

        reply = random_joke()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue

    # ========================================
    # Fact
    # ========================================

    elif user == "fact":

        reply = random_fact()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue

    # ========================================
    # Motivation
    # ========================================

    elif user == "motivate":

        reply = random_quote()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue
"""
chatbot.py
Main Application of DecodeBot v2.1
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
    show_history,
    read_knowledge,
    search_knowledge,
    about,
    goodbye
)

from logger import (
    log_conversation,
    view_log
)

from version import APP_NAME, VERSION

# ============================================
# Initial Setup
# ============================================

clear_screen()

banner()

history = []

print()

name = input("Bot : Hello! What's your name?\nYou : ").strip()

if not name:
    name = "Friend"

bot_print(f"Welcome {name}!")

bot_print(
    f"You are now using {APP_NAME} Version {VERSION}."
)

bot_print(
    "Type 'help' to see all available commands."
)

print()

# ============================================
# Main Loop
# ============================================

while True:

    user = input(f"{name} : ").lower().strip()

    history.append(f"{name}: {user}")

    # ========================================
    # Greetings
    # ========================================

    if user in GREETING_COMMANDS:

        reply = random_greeting()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue

    # ========================================
    # Exit
    # ========================================

    elif user in EXIT_COMMANDS:

        reply = RESPONSES[user]

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        goodbye()

        break

    # ========================================
    # Help
    # ========================================

    elif user == "help":

        show_help()

        history.append("Bot: Help menu shown")

        continue

    # ========================================
    # Calculator
    # ========================================

    elif user == "calculator":

        calculator()

        history.append("Bot: Calculator used")

        continue

    # ========================================
    # Square
    # ========================================

    elif user == "square":

        square()

        history.append("Bot: Square calculated")

        continue

    # ========================================
    # Cube
    # ========================================

    elif user == "cube":

        cube()

        history.append("Bot: Cube calculated")

        continue

    # ========================================
    # Factorial
    # ========================================

    elif user == "factorial":

        factorial()

        history.append("Bot: Factorial calculated")

        continue

    # ========================================
    # Percentage
    # ========================================

    elif user == "percentage":

        percentage()

        history.append("Bot: Percentage calculated")

        continue

    # ========================================
    # Multiplication Table
    # ========================================

    elif user == "table":

        table()

        history.append("Bot: Multiplication table generated")

        continue

    # ========================================
    # Joke
    # ========================================

    elif user == "joke":

        reply = random_joke()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue

    # ========================================
    # Fact
    # ========================================

    elif user == "fact":

        reply = random_fact()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue

    # ========================================
    # Motivation
    # ========================================

    elif user == "motivate":

        reply = random_quote()

        bot_print(reply)

        history.append(f"Bot: {reply}")

        log_conversation(user, reply)

        continue