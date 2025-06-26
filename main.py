from FrontEndAgent import FrontEndAgent

agent = FrontEndAgent()
user_id = "9990"

while True:
    user_message = input("You: ")
    response = agent.handle_message(user_id, user_message)
    print("Bot:", response)
