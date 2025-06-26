class GreetingAgent:
    def handle(self, message):
        if "hello" in message.lower():
            return "Hello Dear! How can I help you today?"
        return None
