responses = {
    'hello': 'Hey! How can I help you?',
    'how are you': 'I am fine, what about you?',
    'what is your name': 'I am an AI chatbot of Decodelabs',
    'what can you do': 'I can answer questions, assist and help you learn',
    'why should i use ai?': 'AI can help you learn faster, save time, and solve problems'
}


print("Type 'exit' to leave." )
while True:
    user = input("You: ").strip().lower()
    if user == 'exit':
        print('Goodbye! Have a nice day.')
        break
    reply = responses.get(user, 'I cannot find this message, type another message.')
    print(reply)