"""
utils.py
Utility functions for DecodeBot
"""

import os
import time
import math
import platform
from datetime import datetime


# ======================================================
# Banner
# ======================================================

def banner():

    try:

        with open("assets/logo.txt", "r", encoding="utf-8") as file:

            print(file.read())

    except FileNotFoundError:

        print("=" * 60)
        print("DecodeBot v2.1")
        print("=" * 60)

    try:

        with open("assets/welcome.txt", "r", encoding="utf-8") as file:

            print(file.read())

    except FileNotFoundError:

        print("Welcome to DecodeBot!")
        print("Type 'help' to see available commands.\n")


# ======================================================
# Typing Effect
# ======================================================

def bot_print(message):

    print("\nBot is typing...", end="", flush=True)

    time.sleep(0.5)

    print("\rBot:", message)


# ======================================================
# Help Menu
# ======================================================

def show_help():

    print("\n" + "=" * 60)

    print("AVAILABLE COMMANDS")

    print("=" * 60)

    try:

        with open("data/commands.txt", "r", encoding="utf-8") as file:

            for line in file:

                print("•", line.strip())

    except FileNotFoundError:

        print("Commands file not found.")

    print("=" * 60)


# ======================================================
# Current Date
# ======================================================

def show_date():

    today = datetime.now()

    bot_print(today.strftime("%d-%m-%Y"))


# ======================================================
# Current Time
# ======================================================

def show_time():

    now = datetime.now()

    bot_print(now.strftime("%I:%M:%S %p"))


# ======================================================
# System Information
# ======================================================

def system_info():

    print("\nSystem Information")

    print("-" * 40)

    print("Operating System :", platform.system())

    print("Release          :", platform.release())

    print("Version          :", platform.version())

    print("Machine          :", platform.machine())

    print("Processor        :", platform.processor())

    print("Python Version   :", platform.python_version())

    print("-" * 40)


# ======================================================
# Clear Screen
# ======================================================

def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


# ======================================================
# Calculator
# ======================================================

def calculator():

    print("\nCalculator")

    print("-" * 40)

    try:

        num1 = float(input("First Number : "))

        operator = input("Operator (+ - * / % // ^): ")

        num2 = float(input("Second Number : "))

        if operator == "+":

            result = num1 + num2

        elif operator == "-":

            result = num1 - num2

        elif operator == "*":

            result = num1 * num2

        elif operator == "/":

            if num2 == 0:

                bot_print("Division by zero is not allowed.")

                return

            result = num1 / num2

        elif operator == "%":

            result = num1 % num2

        elif operator == "//":

            result = num1 // num2

        elif operator == "^":

            result = num1 ** num2

        else:

            bot_print("Invalid Operator.")

            return

        bot_print(f"Result = {result}")

    except ValueError:

        bot_print("Please enter valid numbers.")


# ======================================================
# Square
# ======================================================

def square():

    try:

        number = float(input("Enter Number : "))

        bot_print(f"Square = {number ** 2}")

    except:

        bot_print("Invalid Input")


# ======================================================
# Cube
# ======================================================

def cube():

    try:

        number = float(input("Enter Number : "))

        bot_print(f"Cube = {number ** 3}")

    except:

        bot_print("Invalid Input")


# ======================================================
# Factorial
# ======================================================

def factorial():

    try:

        number = int(input("Enter Integer : "))

        if number < 0:

            bot_print("Factorial not defined.")

            return

        bot_print(f"Factorial = {math.factorial(number)}")

    except:

        bot_print("Invalid Input")


# ======================================================
# Percentage
# ======================================================

def percentage():

    try:

        obtained = float(input("Obtained Marks : "))

        total = float(input("Total Marks : "))

        percent = (obtained / total) * 100

        bot_print(f"Percentage = {percent:.2f}%")

    except:

        bot_print("Invalid Input")


# ======================================================
# Multiplication Table
# ======================================================

def table():

    try:

        number = int(input("Enter Number : "))

        print()

        for i in range(1, 11):

            print(f"{number} x {i} = {number * i}")

    except:

        bot_print("Invalid Input")
# ======================================================
# Mini Quiz
# ======================================================

def quiz():

    score = 0

    print("\n========== AI QUIZ ==========\n")

    answer = input(
        "1. What does AI stand for?\n"
        "a) Artificial Intelligence\n"
        "b) Automated Internet\n"
        "c) Artificial Interface\n\n"
        "Answer: "
    ).lower()

    if answer == "a":
        score += 1

    answer = input(
        "\n2. Python is mainly a...\n"
        "a) Programming Language\n"
        "b) Operating System\n"
        "c) Web Browser\n\n"
        "Answer: "
    ).lower()

    if answer == "a":
        score += 1

    answer = input(
        "\n3. Machine Learning is...\n"
        "a) A Database\n"
        "b) A subset of AI\n"
        "c) A Computer\n\n"
        "Answer: "
    ).lower()

    if answer == "b":
        score += 1

    answer = input(
        "\n4. HTML is used for...\n"
        "a) Styling webpages\n"
        "b) Structuring webpages\n"
        "c) Artificial Intelligence\n\n"
        "Answer: "
    ).lower()

    if answer == "b":
        score += 1

    answer = input(
        "\n5. CSS is mainly used for...\n"
        "a) Designing webpages\n"
        "b) Machine Learning\n"
        "c) Databases\n\n"
        "Answer: "
    ).lower()

    if answer == "a":
        score += 1

    print("\n=============================")
    bot_print(f"You scored {score}/5")

    if score == 5:
        bot_print("Excellent! Perfect Score!")

    elif score >= 3:
        bot_print("Good Job! Keep Learning.")

    else:
        bot_print("Don't worry. Practice makes perfect.")

    print("=============================")


# ======================================================
# Conversation History
# ======================================================

def show_history(history):

    print("\n" + "=" * 60)
    print("CONVERSATION HISTORY")
    print("=" * 60)

    if len(history) == 0:

        print("No conversation available.")

    else:

        for item in history:

            print(item)

    print("=" * 60)


# ======================================================
# Read Knowledge Base
# ======================================================

def read_knowledge():

    print("\n========== KNOWLEDGE ==========\n")

    try:

        with open("data/knowledge.txt", "r", encoding="utf-8") as file:

            print(file.read())

    except FileNotFoundError:

        print("Knowledge file not found.")

    print("=" * 40)


# ======================================================
# Search Knowledge
# ======================================================

def search_knowledge(keyword):

    try:

        with open("data/knowledge.txt", "r", encoding="utf-8") as file:

            for line in file:

                if keyword.lower() in line.lower():

                    return line.strip()

    except FileNotFoundError:

        return "Knowledge base unavailable."

    return "No information found."


# ======================================================
# Read Commands File
# ======================================================

def read_commands():

    try:

        with open("data/commands.txt", "r", encoding="utf-8") as file:

            return [
                line.strip()
                for line in file
                if line.strip()
            ]

    except FileNotFoundError:

        return []


# ======================================================
# About Screen
# ======================================================

def about():

    print("\n" + "=" * 60)

    print("DecodeBot v2.1")

    print("=" * 60)

    print("A Rule-Based Artificial Intelligence Chatbot")

    print("Built using Python")

    print("Developed for DecodeLabs AI Internship")

    print("=" * 60)


# ======================================================
# Goodbye Screen
# ======================================================

def goodbye():

    print()

    print("=" * 60)

    print("Thank you for using DecodeBot!")

    print("Keep Learning.")

    print("Keep Building.")

    print("Goodbye!")

    print("=" * 60)


# ======================================================
# End of File
# ======================================================