# chatbot.py
def chatbot_response(user_input):
    # Simple keyword-based response
    responses = {
        "hi": "Hello, how can I help you?",
        "hello": "Hi there! How can I assist you today?",
        "bye": "Goodbye! Have a nice day!",
    }

    # Return response if keyword found, otherwise default message
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.")
