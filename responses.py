"""
responses.py
Stores chatbot responses and loads dynamic data.
"""

import random
from version import *

# ==========================================================
# Load data from text files
# ==========================================================

def load_data(file_path):
    """
    Reads all non-empty lines from a text file.
    """

    try:

        with open(file_path, "r", encoding="utf-8") as file:

            return [
                line.strip()
                for line in file
                if line.strip()
            ]

    except FileNotFoundError:

        return []


# ==========================================================
# Data Files
# ==========================================================

JOKES = load_data("data/jokes.txt")

FACTS = load_data("data/facts.txt")

QUOTES = load_data("data/quotes.txt")

KNOWLEDGE = load_data("data/knowledge.txt")


# ==========================================================
# Random Generators
# ==========================================================

def random_joke():

    if JOKES:
        return random.choice(JOKES)

    return "No jokes available."


def random_fact():

    if FACTS:
        return random.choice(FACTS)

    return "No facts available."


def random_quote():

    if QUOTES:
        return random.choice(QUOTES)

    return "No motivational quotes available."


# ==========================================================
# Greetings
# ==========================================================

GREETINGS = [

    "Hello! Nice to meet you.",

    "Hi there! Hope you're having a wonderful day.",

    "Greetings! Welcome to DecodeBot.",

    "Hey! How can I assist you today?",

    "Hello! Ready to explore Rule-Based AI?",

    "Welcome back!",

    "Good to see you again!",

    "Hi! Let's learn something new today."

]


def random_greeting():

    return random.choice(GREETINGS)


# ==========================================================
# About Project
# ==========================================================

ABOUT = f"""
Project Name : {APP_NAME}

Version : {VERSION}

Developer : {AUTHOR}

Organization : {ORGANIZATION}

Program : {PROGRAM}

Language : {LANGUAGE}

Project Type : {PROJECT_TYPE}

License : {LICENSE}

Description :

{DESCRIPTION}

GitHub :

{GITHUB}
"""


# ==========================================================
# Fixed Responses
# ==========================================================

RESPONSES = {

    "about": ABOUT,

    "what is your name":
        f"My name is {APP_NAME}.",

    "who created you":
        f"I was created by {AUTHOR}.",

    "what can you do":
        (
            "I can answer predefined questions, "
            "perform calculations, tell jokes, "
            "share AI facts, display the date and time, "
            "conduct quizzes and much more."
        ),

    "ai":
        (
            "Artificial Intelligence enables machines "
            "to perform tasks that normally require "
            "human intelligence."
        ),

    "artificial intelligence":
        (
            "Artificial Intelligence is the simulation "
            "of human intelligence in machines."
        ),

    "machine learning":
        (
            "Machine Learning is a subset of Artificial "
            "Intelligence where systems learn from data."
        ),

    "deep learning":
        (
            "Deep Learning uses multi-layer neural "
            "networks to solve complex problems."
        ),

    "python":
        (
            "Python is a popular programming language "
            "used in AI, Data Science, Web Development "
            "and Automation."
        ),

    "java":
        (
            "Java is an object-oriented programming "
            "language widely used in enterprise software."
        ),

    "c++":
        (
            "C++ is commonly used in game development, "
            "system software and competitive programming."
        ),

    "javascript":
        (
            "JavaScript is used to build interactive "
            "web applications."
        ),

    "html":
        "HTML defines the structure of web pages.",

    "css":
        "CSS is used to style web pages.",

    "i am happy":
        "That's wonderful! Keep smiling and keep learning.",

    "i am sad":
        (
            "I'm sorry you're feeling sad. "
            "Every challenge is temporary."
        ),

    "i am stressed":
        (
            "Take a deep breath, relax for a moment "
            "and believe in yourself."
        ),

    "thank you":
        "You're welcome!",

    "thanks":
        "Happy to help!",

    "bye":
        "Goodbye! Have a wonderful day.",

    "exit":
        "Thank you for using DecodeBot.",

    "quit":
        "Session ended successfully."
}


# ==========================================================
# Commands
# ==========================================================

GREETING_COMMANDS = [

    "hello",
    "hi",
    "hey",
    "good morning",
    "good afternoon",
    "good evening"

]


EXIT_COMMANDS = [

    "bye",
    "exit",
    "quit"

]