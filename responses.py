def get_response(user_input):
    
    user_input = user_input.lower()
    
    responses = {
        "hello": "Hi! How can I help you?",
        "how are you": "I am doing great.",
        "bye": "Goodbye!"
    }
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I do not understand."


if __name__ == "__main__":
    
    print(get_response("hello"))