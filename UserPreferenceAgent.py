class UserPreferenceAgent:
    def __init__(self):
        self.user_data = {}

    def handle(self, user_id, message):
        msg = message.lower().strip()

        if "my name is" in msg:
            name = msg.split("my name is")[-1].strip().capitalize()
            if user_id not in self.user_data:
                self.user_data[user_id] = {}
            self.user_data[user_id]["name"] = name
            return f"Got it! I'll remember that your name is {name}."

        elif "my password is" in msg:
            password = msg.split("my password is")[-1].strip()
            if user_id not in self.user_data:
                self.user_data[user_id] = {}
            self.user_data[user_id]["password"] = password
            return "Thanks! I've saved your password."

        elif "what is my name" in msg:
            if user_id in self.user_data and "name" in self.user_data[user_id]:
                return f"Your name is {self.user_data[user_id]['name']}."
            else:
                return "I don't know your name yet. What is your name?"
        elif "what is my password" in msg:
            if user_id in self.user_data and "password" in self.user_data[user_id]:
                return f"Your password is {self.user_data[user_id]['password']}."
            else:
                return "I don't know your password yet. What is it?"
        return None
