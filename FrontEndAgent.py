from GreetingAgent import GreetingAgent
from UserPreferenceAgent import UserPreferenceAgent

class FrontEndAgent:
    def __init__(self):
        self.greeting_agent = GreetingAgent()
        self.preference_agent = UserPreferenceAgent()

    def handle_message(self, user_id, message):
        response = self.greeting_agent.handle(message)
        if response:
            return response

        response = self.preference_agent.handle(user_id, message)
        if response:
            return response

        return "I can handle greetings or your name for now."
