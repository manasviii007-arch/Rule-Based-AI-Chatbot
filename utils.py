"""
utils.py
Utility functions for DecodeBot
"""

import os
import time
import random
import datetime
import platform
import math

from responses import JOKES, FACTS, MOTIVATION


# ==============================
# ASCII Banner
# ==============================

def banner():

    print("=" * 70)

    with open("assets/logo.txt", "r", encoding="utf-8") as file:
        print(file.read())

    print("=" * 70)

    with open("assets/welcome.txt", "r", encoding="utf-8") as file:
        print(file.read())

    print("=" * 70)


# ==============================
# Typing Effect
# ==============================

def bot_print(message):

    print("\nBot is typing...", end="")
    time.sleep(0.6)

    print("\rBot :", message)


# ==============================
# Help Menu
# ==============================

def show_help():

    print("\n" + "=" * 60)
    print("AVAILABLE COMMANDS")
    print("=" * 60)

    print("\nGeneral")
    print(" hello")
    print(" hi")
    print(" hey")
    print(" help")
    print(" about")

    print("\nKnowledge")
    print(" ai")
    print(" machine learning")
    print(" deep learning")
    print(" python")
    print(" java")
    print(" c++")
    print(" javascript")
    print(" html")
    print(" css")

    print("\nUtilities")
    print(" calculator")
    print(" square")
    print(" cube")
    print(" factorial")
    print(" percentage")
    print(" table")
    print(" date")
    print(" time")
    print(" system")
    print(" clear")

    print("\nEntertainment")
    print(" joke")
    print(" fact")
    print(" motivate")
    print(" quiz")

    print("\nConversation")
    print(" history")
    print(" exit")

    print("=" * 60)


# ==============================
# Random Joke
# ==============================

def tell_joke():
    bot_print(random.choice(JOKES))


# ==============================
# Random Fact
# ==============================

def tell_fact():
    bot_print(random.choice(FACTS))


# ==============================
# Motivation
# ==============================

def motivate():
    bot_print(random.choice(MOTIVATION))


# ==============================
# Date
# ==============================

def show_date():

    today = datetime.datetime.now().strftime("%d-%m-%Y")

    bot_print(f"Today's date is {today}")


# ==============================
# Time
# ==============================

def show_time():

    current = datetime.datetime.now().strftime("%I:%M:%S %p")

    bot_print(f"Current time is {current}")


# ==============================
# System Information
# ==============================

def system_info():

    print("\nSystem Information")
    print("-" * 40)

    print("Operating System :", platform.system())
    print("Release          :", platform.release())
    print("Machine          :", platform.machine())
    print("Processor        :", platform.processor())
    print("Python Version   :", platform.python_version())

    print("-" * 40)


# ==============================
# Clear Screen
# ==============================

def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


# ==============================
# Calculator
# ==============================

def calculator():

    print("\nCalculator")
    print("-" * 30)

    try:

        num1 = float(input("Enter first number : "))
        operator = input("Operator (+ - * / % // ^): ")
        num2 = float(input("Enter second number : "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":

            if num2 == 0:
                bot_print("Cannot divide by zero.")
                return

            result = num1 / num2

        elif operator == "%":
            result = num1 % num2

        elif operator == "//":
            result = num1 // num2

        elif operator == "^":
            result = num1 ** num2

        else:

            bot_print("Invalid operator.")
            return

        bot_print(f"Result = {result}")

    except:

        bot_print("Invalid input.")


# ==============================
# Square
# ==============================

def square():

    try:

        number = float(input("Enter number : "))

        bot_print(f"Square = {number ** 2}")

    except:

        bot_print("Invalid input.")


# ==============================
# Cube
# ==============================

def cube():

    try:

        number = float(input("Enter number : "))

        bot_print(f"Cube = {number ** 3}")

    except:

        bot_print("Invalid input.")


# ==============================
# Factorial
# ==============================

def factorial():

    try:

        number = int(input("Enter integer : "))

        if number < 0:

            bot_print("Factorial not defined.")

        else:

            bot_print(f"Factorial = {math.factorial(number)}")

    except:

        bot_print("Invalid input.")


# ==============================
# Percentage
# ==============================

def percentage():

    try:

        obtained = float(input("Obtained Marks : "))
        total = float(input("Total Marks : "))

        percent = (obtained / total) * 100

        bot_print(f"Percentage = {percent:.2f}%")

    except:

        bot_print("Invalid input.")


# ==============================
# Multiplication Table
# ==============================

def table():

    try:

        number = int(input("Enter number : "))

        print()

        for i in range(1, 11):

            print(f"{number} x {i} = {number*i}")

    except:

        bot_print("Invalid input.")


# ==============================
# Quiz
# ==============================

def quiz():

    score = 0

    print("\nMini AI Quiz\n")

    answer = input(
        "1. What does AI stand for?\n"
        "a) Artificial Intelligence\n"
        "b) Automated Internet\n"
        "c) Artificial Interface\n\n"
        "Answer : "
    ).lower()

    if answer == "a":
        score += 1

    answer = input(
        "\n2. Python is a...\n"
        "a) Snake only\n"
        "b) Programming Language\n"
        "c) Operating System\n\n"
        "Answer : "
    ).lower()

    if answer == "b":
        score += 1

    answer = input(
        "\n3. Machine Learning is...\n"
        "a) A subset of AI\n"
        "b) A Web Browser\n"
        "c) A Database\n\n"
        "Answer : "
    ).lower()

    if answer == "a":
        score += 1

    bot_print(f"You scored {score}/3")


# ==============================
# Chat History
# ==============================

def show_history(history):

    print("\nConversation History")
    print("-" * 40)

    if len(history) == 0:

        print("No conversation yet.")

    else:

        for message in history:

            print(message)

    print("-" * 40)


# ==============================
# Save Chat
# ==============================

def save_chat(user, bot):

    with open("chat_history.txt", "a", encoding="utf-8") as file:

        file.write(f"You : {user}\n")

        file.write(f"Bot : {bot}\n")

        file.write("-" * 40 + "\n")