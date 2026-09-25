def chatbot():
    print("================================")
    print("       🤖 BASIC CHATBOT")
    print("================================")
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm fine! Thanks for asking.")

        elif user_input == "thanks":
            print("Bot: You're welcome!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
