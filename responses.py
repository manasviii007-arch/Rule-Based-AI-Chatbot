"""
responses.py
Stores predefined responses and loads dynamic content from data files.
"""

import random

# ==========================================================
# Helper Function
# ==========================================================

def load_random_line(file_path):
    """
    Load a random non-empty line from a text file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]

        return random.choice(lines)

    except FileNotFoundError:
        return "Data file not found."

    except Exception as e:
        return f"Error: {e}"


# ==========================================================
# Dynamic Responses
# ==========================================================

def random_joke():
    return load_random_line("data/jokes.txt")


def random_fact():
    return load_random_line("data/facts.txt")


def random_quote():
    return load_random_line("data/quotes.txt")


# ==========================================================
# Greeting Responses
# ==========================================================

GREETINGS = [

    "Hello! Nice to meet you.",

    "Hi there! Hope you're having a wonderful day.",

    "Greetings! How can I help you today?",

    "Welcome! I'm DecodeBot.",

    "Hey! Ready to explore Rule-Based AI?",

    "Hello! Let's build something amazing today.",

    "Hi! What can I do for you?",

    "Welcome back!",

    "Nice to see you again!",

    "Hello! Hope you're having a productive day."
]


def random_greeting():
    return random.choice(GREETINGS)


# ==========================================================
# Fixed Responses
# ==========================================================

RESPONSES = {

    # About
    "what is your name":
        "My name is DecodeBot. I am a Rule-Based AI Chatbot developed using Python.",

    "who created you":
        "I was created by Manasvi Chugh as part of the DecodeLabs Artificial Intelligence Internship.",

    "what can you do":
        "I can answer predefined questions, tell jokes, share AI facts, perform calculations, conduct quizzes and much more.",

    "about":
        """Project : DecodeBot v2.0
Developer : Manasvi Chugh
Language : Python
Type : Rule-Based Artificial Intelligence Chatbot
Internship : DecodeLabs Artificial Intelligence Industrial Training Program""",

    # Artificial Intelligence
    "ai":
        """Artificial Intelligence enables machines to simulate human intelligence such as learning, reasoning and decision making.""",

    "artificial intelligence":
        """Artificial Intelligence is the science of building intelligent computer systems capable of solving real-world problems.""",

    "machine learning":
        """Machine Learning is a subset of Artificial Intelligence where computers learn patterns from data.""",

    "deep learning":
        """Deep Learning is a branch of Machine Learning that uses neural networks with multiple layers.""",

    # Programming Languages
    "python":
        "Python is a high-level programming language widely used for AI, Data Science, Automation and Web Development.",

    "java":
        "Java is an object-oriented programming language used in enterprise software and Android development.",

    "c++":
        "C++ is a powerful programming language used in system software, game development and competitive programming.",

    "javascript":
        "JavaScript is the programming language used to build interactive websites.",

    "html":
        "HTML stands for HyperText Markup Language and defines the structure of webpages.",

    "css":
        "CSS stands for Cascading Style Sheets and is used to style webpages.",

    # Feelings
    "i am happy":
        "That's wonderful! Keep smiling and continue learning every day.",

    "i am sad":
        "I'm sorry you're feeling sad. Every challenge is temporary. Keep believing in yourself.",

    "i am stressed":
        "Take a deep breath, drink some water and remember to take short breaks while studying.",

    "i am bored":
        "How about solving a coding problem or learning a new Python concept?",

    # Thanks
    "thanks":
        "You're welcome! Happy coding!",

    "thank you":
        "You're always welcome!",

    # Goodbye
    "bye":
        "Goodbye! Have a wonderful day.",

    "exit":
        "Thank you for using DecodeBot. Keep learning and building amazing projects!",

    "quit":
        "Session ended. See you next time!"
}

# ==========================================================
# Greeting Commands
# ==========================================================

GREETING_COMMANDS = [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good afternoon",
    "good evening"
]

# ==========================================================
# Exit Commands
# ==========================================================

EXIT_COMMANDS = [
    "bye",
    "exit",
    "quit"
]