print("Welcome to the QA Bot!")
print("You can ask me about HKU, robot, Jetson, AI, human, Python, coding, or technology.")
print("Type 'help' to see keywords.")
print("Type 'bye' to exit.")

while True:
    question = input("\nPlease enter your question: ")
    question = question.lower()

    if question == "bye":
        print("Goodbye! Have a nice day!")
        break

    elif question == "help":
        print("You can ask about:")
        print("- HKU")
        print("- robot")
        print("- Jetson")
        print("- AI")
        print("- human")
        print("- Python")
        print("- coding")
        print("- technology")

    elif "hello" in question or "hi" in question:
        print("Hello! Nice to meet you!")

    elif "hku" in question:
        print("HKU stands for The University of Hong Kong.")

    elif "robot" in question:
        print("A robot is a machine that can perform tasks automatically.")

    elif "jetson" in question:
        print("NVIDIA Jetson is a small computer platform used for AI and robotics.")

    elif "ai" in question:
        print("AI stands for Artificial Intelligence.")
        print("AI allows computers to learn, think, and solve problems.")

    elif "human" in question:
        print("Humans can think, learn, communicate, and make decisions.")

    elif "python" in question:
        print("Python is a popular programming language.")
        print("It is easy to learn and is often used for AI and robotics.")

    elif "coding" in question or "programming" in question:
        print("Coding means writing instructions for a computer to follow.")

    elif "technology" in question:
        print("Technology uses science and engineering to solve problems.")

    elif "name" in question:
        print("My name is QA Bot!")

    elif "how are you" in question:
        print("I am doing great! Thank you for asking.")

    else:
        print("Sorry, I don't know the answer to that question.")
        print("Type 'help' to see what you can ask me.")

