from responses import get_response

def start_chat():
    
    print("Chatbot started (type 'exit' to stop)")
    
    while True:
        
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        
        response = get_response(user_input)
        
        print("Bot:", response)


if __name__ == "__main__":
    start_chat()