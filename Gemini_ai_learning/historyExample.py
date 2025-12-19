# There is no setup for History in this code example.
import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')
def chatbot():
    """Simple chatbot using Gemini"""
    print("=" * 60)
    print("           AI CHATBOT")
    print("=" * 60)
    print("Type 'quit' to exit")
    print("=" * 60)
    while True:
        # Get user input
        user_input = input("\nYou: ")
        # Check for exit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        # Skip empty input
        if not user_input.strip():
            continue
        try:
            # Generate response
            response = model.generate_content(user_input)
            print(f"Chatbot: {response.text}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    chatbot()
