import google.generativeai as genai


class ConversationalChatbot:
    def __init__(self, api_key):
        """Initialize chatbot with conversation memory"""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.chat_session = self.model.start_chat(history=[])

    def send_message(self, message):
        """Send message and get response"""
        try:
            response = self.chat_session.send_message(message)
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def get_history(self):
        """Get conversation history"""
        return self.chat_session.history

    def clear_history(self):
        """Start a new conversation"""
        self.chat_session = self.model.start_chat(history=[])

    def chat(self):
        """Interactive chat with memory"""
        print("\n" + "=" * 60)
        print("      CONVERSATIONAL AI (WITH MEMORY)")
        print("=" * 60)
        print("I remember our conversation!")
        print("Commands: 'quit', 'history', 'clear'")
        print("=" * 60)
        while True:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
            if user_input.lower() == 'quit':
                print("Chatbot: Goodbye!")
                break
            if user_input.lower() == 'history':
                print("\nConversation History:")
                print("-" * 60)
                for msg in self.chat_session.history:
                    role = "You" if msg.role == "user" else "AI"
                    print(f"{role}: {msg.parts[0].text}")
                print("-" * 60)
                continue
            if user_input.lower() == 'clear':
                self.clear_history()
                print("Chatbot: Memory cleared! Starting fresh.")
                continue
            response = self.send_message(user_input)
            print(f"\nChatbot: {response}")


if __name__ == "__main__":
    from config import GEMINI_API_KEY

    chatbot = ConversationalChatbot(api_key=GEMINI_API_KEY)
    chatbot.chat()
