def simple_chatbot():
    """
    A simple rule-based chatbot that responds to predefined inputs.
    """
    print("Chatbot: Hello! I'm a simple rule-based chatbot. You can say 'hello', 'how are you', or 'bye'.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exit the loop to end the conversation
        else:
            print("Chatbot: I'm sorry, I don't understand that. Please try 'hello', 'how are you', or 'bye'.")

simple_chatbot()
