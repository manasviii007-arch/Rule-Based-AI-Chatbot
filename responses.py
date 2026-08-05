"""
responses.py
Contains all predefined responses for DecodeBot.
"""

import random

# ----------------------------
# Random Greetings
# ----------------------------

GREETINGS = [
    "Hello! Nice to meet you.",
    "Hi there! Hope you're having a wonderful day.",
    "Greetings! How can I help you today?",
    "Welcome! I'm DecodeBot.",
    "Hey! Ready to explore Rule-Based AI?"
]

# ----------------------------
# Motivation Quotes
# ----------------------------

MOTIVATION = [
    "Success is the sum of small efforts repeated every day.",
    "Dream big. Start small. Act now.",
    "Learning never exhausts the mind.",
    "Every expert was once a beginner.",
    "Stay curious and keep building.",
    "Believe in yourself.",
    "Practice makes progress.",
    "Consistency beats motivation.",
    "Small improvements every day lead to big results.",
    "Your future is created by what you do today."
]

# ----------------------------
# Programming Jokes
# ----------------------------

JOKES = [

    "Why do programmers prefer dark mode? Because light attracts bugs!",

    "Debugging is like being the detective in a crime movie where you are also the murderer.",

    "Why did Python break up with Java? Because Java had too many classes.",

    "A SQL query walks into a bar and asks: Can I join you?",

    "Why was the computer cold? It forgot to close Windows.",

    "Programmers don't make mistakes. They create unexpected features.",

    "There are only 10 kinds of people: those who understand binary and those who don't.",

    "AI won't replace programmers. It will replace programmers who refuse to learn.",

    "Keyboard not found. Press F1 to continue.",

    "Why did the developer go broke? Because he used up all his cache."
]

# ----------------------------
# Fun Facts
# ----------------------------

FACTS = [

    "Artificial Intelligence was officially introduced in 1956.",

    "Python was created by Guido van Rossum.",

    "Python was first released in 1991.",

    "NASA uses Artificial Intelligence in space research.",

    "Machine Learning is a subset of Artificial Intelligence.",

    "The first computer bug was an actual moth.",

    "Python is named after Monty Python, not the snake.",

    "Rule-Based AI is one of the oldest forms of AI.",

    "Robots can perform surgeries with incredible precision.",

    "AI is used in self-driving cars, healthcare, finance and education."
]

# ----------------------------
# Knowledge Base
# ----------------------------

RESPONSES = {

    # Greetings
    "hi": random.choice(GREETINGS),
    "hello": random.choice(GREETINGS),
    "hey": random.choice(GREETINGS),

    # About
    "what is your name":
        "My name is DecodeBot. I am a Rule-Based AI Chatbot developed using Python.",

    "who created you":
        "I was created by Manasvi Chugh as part of the DecodeLabs AI Internship.",

    "what can you do":
        "I can chat, answer predefined questions, tell jokes, show facts, perform calculations and more.",

    "about":
        """Project : DecodeBot v2.0
Developer : Manasvi Chugh
Language : Python
Type : Rule-Based AI Chatbot
Internship : DecodeLabs Artificial Intelligence Training""",

    # AI
    "ai":
        "Artificial Intelligence enables computers to simulate human intelligence.",

    "machine learning":
        "Machine Learning is a subset of AI that allows computers to learn from data.",

    "deep learning":
        "Deep Learning is a branch of Machine Learning based on neural networks.",

    "python":
        "Python is one of the most popular programming languages for AI and Data Science.",

    "java":
        "Java is an object-oriented programming language widely used for enterprise software.",

    "c++":
        "C++ is a powerful language used in game development and high-performance applications.",

    "javascript":
        "JavaScript is the programming language of the web.",

    "html":
        "HTML is used to structure webpages.",

    "css":
        "CSS is used to style webpages.",

    # Feelings
    "i am happy":
        "That's wonderful! Keep smiling and continue learning.",

    "i am sad":
        "I'm sorry you're feeling sad. Remember that every challenge is temporary.",

    "i am stressed":
        "Take a deep breath, drink some water and take a short break.",

    # Thanks
    "thanks":
        "You're welcome!",

    "thank you":
        "Happy to help!",

    # Goodbye
    "bye":
        "Goodbye! Have a wonderful day.",

    "exit":
        "Goodbye! Keep learning and building amazing projects!",

    "quit":
        "See you next time!"
}