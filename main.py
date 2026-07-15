# to store the responses of user and their reply
responses = {
    'hello': 'Hey! How can I help you?',
    'hey': 'Hello, What help can i do today?',
    'hi': 'Welcome user! How may i assist you?',
    'how are you': 'I am fine, what about you?',
    'what is your name': 'I am an AI chatbot of Decodelabs',
    'what can you do': 'I can answer questions, assist and help you learn',
    'why should i use ai?': 'AI can help you learn faster, save time, and solve problems'
}

# to print this line everytime at the start when a user asks something
print("Welcome! I am an AI chatbot of Decodelabs. You can ask me questions. Type 'exit' to leave." )

# to run until the user types exit
while True:
    
    # whatever the user types, it becomes lowercase
    user = input("You: ").strip().lower()
    
    # if user wants to break
    if user == 'exit':
        print('Goodbye! Have a nice day.')
        break
    
    # if user types a message not stored in responses
    reply = responses.get(user, 'I cannot find this message, type another message.')
    
    # final reply to output
    final_reply = f"Chatbot: {reply}"
    print(final_reply)