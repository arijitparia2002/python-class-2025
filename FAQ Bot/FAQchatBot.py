import gradio as gr
from transformers import pipeline

# Load QA model
print("Loading QA model...")
qa_model = pipeline("question-answering")
print("Model loaded successfully!")

# FAQ context structured as clear Q&A pairs for better extraction

context = ''

with open('C:\\Users\\ariji\\Desktop\\Ai Class PPT\\Ai Class Python Codes\\FAQ Bot\\pharmaFAQ.txt', 'r', encoding='utf-8') as file:
    context = file.read()
    
def chat_response(message, history):
    """Chatbot response function using transformer QA model"""
    if not message.strip():
        return "Please ask me a question about medicines, orders, delivery, or our services."

    try:
        # Use the transformer QA model to answer the question
        result = qa_model(question=message, context=context)
        answer = result['answer']

        return answer

    except Exception as e:
        return "I'm having trouble processing your question. Please try rephrasing it or contact our support team at +91-9876543210 for immediate assistance."

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