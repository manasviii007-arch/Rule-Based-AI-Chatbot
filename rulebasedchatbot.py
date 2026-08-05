# ==========================================================
# PROJECT 1 : RULE-BASED AI CHATBOT
# Artificial Intelligence Internship
# DecodeLabs
# Developed By : MANASVI CHUGH
# ==========================================================

import datetime

print("=" * 65)
print(" WELCOME TO DECODEBOT")
print("=" * 65)
print("Hello! I am DecodeBot, your Rule-Based AI Assistant.")
print("Type 'help' anytime to see what I can do.")
print("Type 'exit' to end the conversation.\n")

while True:

    user = input("You : ").lower().strip()

    # EXIT COMMANDS
    
    if user in ["exit", "bye", "quit", "goodbye"]:

        print("\nBot : Thank you for chatting with me.")
        print("Bot : Have a wonderful day!")
        break

    # GREETINGS

    elif user in ["hi", "hello", "hey", "hii", "hola"]:

        hour = datetime.datetime.now().hour

        if hour < 12:
            print("Bot :  Good Morning!")
        elif hour < 17:
            print("Bot :  Good Afternoon!")
        else:
            print("Bot :  Good Evening!")

        print("Bot : Nice to meet you!")

    # HELP MENU

    elif user == "help":

        print("\n========== HELP MENU ==========")
        print("Greetings")
        print("  hello")
        print("  hi")
        print("  hey")

        print("\nAbout Me")
        print("  what is your name")
        print("  who created you")
        print("  what can you do")

        print("\nKnowledge")
        print("  ai")
        print("  machine learning")
        print("  python")

        print("\nEntertainment")
        print("  joke")
        print("  fact")

        print("\nCalculator")
        print("  calculator")

        print("\nUtilities")
        print("  time")
        print("  date")

        print("\nFeelings")
        print("  i am happy")
        print("  i am sad")
        print("  i am stressed")

        print("\nNested Menu")
        print("  menu")

        print("\nExit")
        print("  exit")
        print("===============================\n")

    # ABOUT BOT

    elif user == "what is your name":

        print("Bot : My name is DecodeBot.")

    elif user == "who created you":

        print("Bot : I was created using Python and Rule-Based AI logic.")

    elif user == "what can you do":

        print("Bot : I can chat, answer FAQs, tell jokes,")
        print("      perform calculations, show date & time,")
        print("      and respond using predefined rules.")

    # AI FAQ

    elif user == "ai":

        print("Bot : AI stands for Artificial Intelligence.")
        print("Bot : It enables machines to simulate human intelligence.")

    elif user == "machine learning":

        print("Bot : Machine Learning is a subset of AI")
        print("Bot : where computers learn from data.")

    elif user == "python":

        print("Bot : Python is one of the most popular")
        print("Bot : programming languages for AI.")

    # DATE & TIME

    elif user == "time":

        print("Bot :", datetime.datetime.now().strftime("%I:%M:%S %p"))

    elif user == "date":

        print("Bot :", datetime.datetime.now().strftime("%d-%m-%Y"))

    # JOKES

    elif user == "joke":

        print("Bot : Why do programmers prefer dark mode?")
        print("Bot : Because light attracts bugs!")

    # FACTS

    elif user == "fact":

        print("Bot : The first AI program was developed")
        print("Bot : in the 1950s.")

    # SENTIMENT ANALYSIS

    elif user == "i am happy":

        print("Bot :  That's wonderful!")
        print("Bot : Keep smiling!")

    elif user == "i am sad":

        print("Bot :  I'm sorry you're feeling sad.")
        print("Bot : Tomorrow is another opportunity.")
        print("Bot : Keep believing in yourself.")

    elif user == "i am stressed":

        print("Bot :  Take a short break.")
        print("Bot : Drink some water.")
        print("Bot : You've got this!")

    # THANKS

    elif user in ["thanks", "thank you"]:

        print("Bot : You're most welcome! ")

    # SIMPLE CALCULATOR

    elif user == "calculator":

        print("\nCalculator")
        print("Operations : +  -  *  /")

        try:

            num1 = float(input("Enter first number : "))
            op = input("Enter operator : ")
            num2 = float(input("Enter second number : "))

            if op == "+":
                print("Result :", num1 + num2)

            elif op == "-":
                print("Result :", num1 - num2)

            elif op == "*":
                print("Result :", num1 * num2)

            elif op == "/":

                if num2 == 0:
                    print("Cannot divide by zero.")

                else:
                    print("Result :", num1 / num2)

            else:
                print("Invalid operator.")

        except:

            print("Invalid Input.")

    # NESTED MENU

    elif user == "menu":

        print("\nChoose a topic")
        print("1. Technology")
        print("2. Motivation")
        print("3. Programming")

        choice = input("Enter choice : ")

        if choice == "1":

            print("Bot : AI, Robotics and Cloud Computing")
            print("Bot : are transforming industries.")

        elif choice == "2":

            print("Bot : Success comes from consistency,")
            print("Bot : not perfection.")

        elif choice == "3":

            print("Bot : Practice coding every day.")
            print("Bot : Small improvements lead to mastery.")

        else:

            print("Bot : Invalid choice.")

    # UNKNOWN INPUT

    else:

        print("Bot : Sorry, I don't understand that.")
        print("Bot : Type 'help' to see available commands.\n")