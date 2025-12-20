import google.generativeai as genai
import gradio as gr
from config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Load FAQ context from file
print("Loading FAQ context...")
try:
    with open('C:\\Users\\ariji\\Desktop\\Ai Class PPT\\Ai Class Python Codes\\FAQ Bot\\pharmaFAQ.txt', 'r', encoding='utf-8') as file:
        faq_context = file.read()
    print("FAQ context loaded successfully!")
except FileNotFoundError:
    print("Warning: pharmaFAQ.txt not found. Using default context.")
    faq_context = "Please add your FAQ content to pharmaFAQ.txt file."


class GeminiFAQChatbot:
    def __init__(self, api_key, faq_context):
        """Initialize Gemini FAQ chatbot"""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.faq_context = faq_context
        self.chat_history = []
        
        # System prompt for the chatbot
        self.system_prompt = f"""You are a helpful pharmaceutical healthcare assistant for YourPharmaHealthcare.
        
Your role is to answer customer questions about medicines, orders, delivery, payments, prescriptions, and services.

FAQ CONTEXT:
{faq_context}

INSTRUCTIONS:
1. Answer questions based ONLY on the FAQ context provided above
2. Be friendly, professional, and helpful
3. If you don't know the answer, direct customers to call +91-9876543210 for support
4. Keep responses concise and clear
5. Always maintain a helpful tone
6. For medical advice, recommend consulting with a pharmacist or doctor"""

    def get_response(self, user_message):
        """Get response from Gemini API"""
        try:
            # Add user message to history
            self.chat_history.append({
                "role": "user",
                "parts": [user_message]
            })
            
            # Create chat session with history
            chat = self.model.start_chat(history=self.chat_history)
            
            # Send message with system prompt context
            response = chat.send_message(
                f"{self.system_prompt}\n\nCustomer Question: {user_message}",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.5,
                    top_p=0.9,
                    max_output_tokens=512
                )
            )
            
            assistant_response = response.text
            
            # Add assistant response to history
            self.chat_history.append({
                "role": "model",
                "parts": [assistant_response]
            })
            
            return assistant_response
            
        except Exception as e:
            return f"I'm having trouble processing your question. Please try rephrasing it or contact our support team at +91-9876543210 for immediate assistance. Error: {str(e)}"

    def clear_history(self):
        """Clear chat history for new conversation"""
        self.chat_history = []

# main codes to run the Gradio interface############################################
# Initialize chatbot
chatbot = GeminiFAQChatbot(api_key=GEMINI_API_KEY, faq_context=faq_context)


def chat_response(message, history):
    """Chatbot response function for Gradio interface"""
    if not message.strip():
        return "Please ask me a question about medicines, orders, delivery, or our services."
    
    return chatbot.get_response(message)


def clear_chat():
    """Clear conversation history"""
    chatbot.clear_history()
    return "Conversation cleared!"


# Create Gradio ChatInterface
demo = gr.ChatInterface(
    fn=chat_response,
    title="YourPharmaHealthcare - FAQ Bot",
    description="Ask me anything about medicines, orders, delivery, payments, prescriptions, and our services. I'm here to help 24/7!",
    examples=[
        "What is your delivery time?",
        "How do I upload my prescription?",
        "Can I return medicines?",
        "What payment methods do you accept?",
        "Do you offer same-day delivery?",
        "How do I track my order?",
        "Can I get consultation from a pharmacist?",
        "Do you deliver to my area?",
        "How much is delivery charge?",
        "Do you require prescription for all medicines?",
    ],
    theme=gr.themes.Soft(),
    chatbot=gr.Chatbot(height=500),
    textbox=gr.Textbox(placeholder="Ask your question here...", container=False, scale=7),
)

if __name__ == "__main__":
    demo.launch(share=True)