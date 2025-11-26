import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# Page config
st.set_page_config(page_title="Travel Planner AI", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS
st.markdown("""
    <style>
    .main {
        max-width: 750px;
        margin: 0 auto;
    }
    h1 {
        text-align: center;
        font-size: 32px;
        margin-bottom: 5px;
        color: #1f77b4;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 13px;
        margin-bottom: 20px;
    }
    .footer-text {
        text-align: center;
        font-size: 12px;
        color: #888;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>🧳 Travel Planner AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Your personal travel planning assistant</p>", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pipe" not in st.session_state:
    with st.spinner("Loading conversational AI model..."):
        try:
            # Using DialoGPT which is specifically trained for conversations
            st.session_state.pipe = pipeline(
                "text-generation",
                model="microsoft/DialoGPT-small",
                device=-1
            )
        except:
            # Fallback to gpt2
            st.session_state.pipe = pipeline(
                "text-generation",
                model="gpt2",
                device=-1
            )

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input area
user_input = st.chat_input("Ask me about your trip...", key="chat_input")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Planning..."):
            try:
                # Build conversation history for context
                history = ""
                for msg in st.session_state.messages[-6:]:  # Last 6 messages for context
                    if msg["role"] == "user":
                        history += f"User: {msg['content']}\n"
                    else:
                        history += f"Assistant: {msg['content']}\n"
                
                # Add context about being a travel assistant
                prompt = f"""You are a friendly and helpful travel planning assistant. 
Your job is to help people plan amazing trips by suggesting destinations, activities, travel tips, and itineraries.
Always be enthusiastic about travel and give specific, useful advice.

Conversation:
{history}
Assistant:"""
                
                response = st.session_state.pipe(
                    prompt,
                    max_length=150,
                    num_return_sequences=1,
                    temperature=0.9,
                    top_p=0.95,
                    do_sample=True,
                    truncation=True
                )
                
                generated_text = response[0]["generated_text"]
                
                # Extract just the assistant's response
                if "Assistant:" in generated_text:
                    generated_text = generated_text.split("Assistant:")[-1].strip()
                
                # Remove any continuation of conversation
                if "User:" in generated_text:
                    generated_text = generated_text.split("User:")[0].strip()
                
                # Clean up
                generated_text = generated_text.strip()
                
                # Fallback responses based on user input
                if not generated_text or len(generated_text) < 8:
                    user_lower = user_input.lower()
                    
                    if "hello" in user_lower or "hi" in user_lower or "how are you" in user_lower:
                        generated_text = "Hello! 👋 I'm excited to help you plan an amazing trip! Where are you thinking of traveling, or would you like some destination suggestions?"
                    
                    elif "where" in user_lower:
                        generated_text = "Great question! I'd be happy to suggest destinations. Tell me about your preferences - do you like beaches, mountains, cities, or cultural sites? What's your budget and when are you planning to travel?"
                    
                    elif "when" in user_lower:
                        generated_text = "The best time to travel depends on your destination. Summer is great for Europe, winter for ski resorts, and shoulder seasons offer good weather and fewer crowds. Where are you thinking of going?"
                    
                    elif "budget" in user_lower or "cost" in user_lower:
                        generated_text = "Budget travel is totally possible! Southeast Asia, Central America, and Eastern Europe offer incredible value. I can help you find affordable flights, accommodations, and activities. What's your budget range?"
                    
                    else:
                        generated_text = f"That's interesting! Tell me more about what you're looking for in your trip - destination, season, activities, or budget? I'm here to help you plan something amazing!"
                
                st.write(generated_text)
                
            except Exception as e:
                generated_text = "Let me help you with your travel plans! Could you tell me more about your destination, dates, or what kind of experience you're looking for?"
                st.write(generated_text)
    
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": generated_text})
    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<p class='footer-text'>
💡 Try asking: "I want to visit Europe" • "Best beaches in Asia?" • "Budget travel tips" • "Two-week itinerary"
</p>
""", unsafe_allow_html=True)
