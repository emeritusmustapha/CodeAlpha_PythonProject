def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi there"
    elif "how are you" in user_input:
        return "I'm doing alright, thanks for asking"
    elif "your name" in user_input:
        return "I'm just a simple chatbot"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye"
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome"
    else:
        return "Sorry, I don't understand that"

print("Chatbot ready. Type 'bye' to exit.")

while True:
    user = input("\nYou: ")
    reply = chatbot_response(user)
    print("Bot:", reply)
    
    if reply == "Goodbye":
        break
