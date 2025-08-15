print("HEllo! I am ChatBot. Type 'bye' to exit.")

while True:
    user=input("You:").lower()

    if user == "hi" or user == "hello":
        print("Bot:Hello there! How can I help you today?")

    elif user=="how are you":
        print("Bot: I am just a bunch of code, but I am doing great! How about you?")

    elif user=="I am fine" or user=="fine":
        print("Bot: Glad to hear that!")

    elif user=="What is your name":
        print("Bot: I am ChatBot, your friendly assistant.")

    elif user=="bye":
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: sorry, I didn't understand that.")
