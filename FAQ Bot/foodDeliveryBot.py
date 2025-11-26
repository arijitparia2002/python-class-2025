import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="FoodExpress - FAQ Chatbot",
    page_icon="🍔",
    layout="centered"
)

# Load QA model (with caching to avoid reloading)
@st.cache_resource
def load_model():
    print("Loading QA model...")
    model = pipeline("question-answering")
    print("Model loaded successfully!")
    return model

qa_model = load_model()

# FAQ context structured as clear Q&A pairs for better extraction
context = """
Q: What restaurants are available on FoodExpress?
A: We partner with over 5000 restaurants including fast food chains, fine dining, local eateries, cloud kitchens, bakeries, dessert shops, and beverage outlets. Available cuisines include Indian, Chinese, Italian, Mexican, Thai, Japanese, Continental, and many more. You can browse by cuisine type, rating, delivery time, or price range.

Q: How do I place an order on FoodExpress?
A: You can place an order through our mobile app or website. Browse restaurants, explore menus, add items to cart, apply coupon codes, and proceed to checkout. Enter your delivery address, choose payment method, and confirm. You'll receive order confirmation with estimated delivery time via SMS and app notification immediately.

Q: What is the delivery time?
A: Average delivery time is 30-45 minutes depending on restaurant preparation time and distance. Some restaurants offer express delivery in 20-25 minutes. You can track your order in real-time. Peak hours like lunch (12-2 PM) and dinner (7-10 PM) may have slightly longer delivery times.

Q: How much are the delivery charges?
A: Delivery charges are typically Rs. 20-50 for orders above Rs. 149. Free delivery is available on orders above Rs. 299 from select restaurants. Surge pricing may apply during peak hours and bad weather. Premium members get free delivery on all orders.

Q: What payment methods do you accept?
A: We accept credit cards, debit cards, UPI (Google Pay, PhonePe, Paytm, BHIM), net banking, digital wallets, cash on delivery, FoodExpress wallet, and meal vouchers from Sodexo. All online payments are secured with SSL encryption and PCI-DSS compliance.

Q: How do I get discounts and offers?
A: Get discounts through promotional codes on our app homepage, bank card offers, first-time user discounts up to 60%, restaurant-specific deals, combo meal offers, and cashback on wallet payments. Subscribe to FoodExpress Pro for exclusive deals. Refer friends to earn cashback rewards.

Q: How do I cancel my order?
A: You can cancel within 60 seconds of placing for free. After that, cancellation depends on order status. If restaurant hasn't started preparation, cancel with minimal charges. Once preparation starts, cancellation may not be possible or will incur charges. Refunds are processed within 5-7 business days.

Q: Can I modify my order after placing it?
A: You can modify within 2 minutes of placing if restaurant hasn't confirmed. Contact customer support at +91-8888888888 for urgent modifications. Changes to address, items, or instructions can be made during this window. After restaurant confirmation, modifications require cancellation and new order.

Q: Do you offer contactless delivery?
A: Yes, we offer contactless delivery. Delivery partner places order at your doorstep, rings the bell, and steps back. Add special delivery instructions like "leave at gate" or "call on arrival" in the app. No-contact delivery is default but you can choose in-person delivery.

Q: How do I track my order?
A: Track your order in real-time through our app. See live updates when restaurant accepts order, food preparation progress, delivery partner pickup, and live GPS tracking of delivery location. You'll receive notifications at each stage. Estimated delivery time updates dynamically.

Q: What if I receive wrong or poor quality food?
A: Report immediately through app within 15 minutes of delivery. Click "Help" section, select your order, and raise issue with photos if possible. We'll investigate and provide refund, credits, or replacement based on the situation. Customer satisfaction is our priority.

Q: What if my order is late?
A: If your order is significantly delayed beyond estimated time, you may be eligible for refund or credits. Contact support through app chat or call +91-8888888888. We'll track the issue and compensate appropriately. During peak hours and bad weather, delays may occur.

Q: Can I add allergy or dietary preferences?
A: Yes, add special instructions for allergies, dietary restrictions, or customization in "Cooking Instructions" field while placing order. Please verify with restaurant directly for severe allergies. Our app allows filtering restaurants by vegetarian, vegan, gluten-free, and other dietary preferences.

Q: How do I rate restaurants and write reviews?
A: Rate restaurants and delivery experience after each order on 5-star scale. Write detailed reviews to help other customers. View restaurant ratings, reviews, hygiene ratings, and popular dishes before ordering. We verify reviews to ensure authenticity.

Q: How do I contact customer support?
A: Our customer support is available 24/7 via in-app chat, phone at +91-8888888888, and email at support@foodexpress.com. Get help with orders, payments, refunds, account issues, and restaurant queries. Average response time is under 5 minutes. Premium members get priority support.

Q: What areas do you deliver to?
A: We deliver across all major areas in metro cities and expanding to tier-2 cities. Enter your delivery address or pincode in app to check serviceability. Coverage includes residential areas, offices, hotels, and outdoor locations. We're continuously adding new zones.

Q: What is the minimum order value?
A: Minimum order value varies by restaurant, typically Rs. 99 to Rs. 149. Some premium restaurants may have higher minimums. This information is displayed on restaurant page before ordering. Partner restaurants set their own minimum order policies.

Q: What is FoodExpress Pro membership?
A: FoodExpress Pro membership costs Rs. 149 per month or Rs. 999 per year. Benefits include unlimited free delivery, exclusive discounts, priority customer support, early access to new restaurants, special member-only deals, and no surge pricing even during peak hours.

Q: How can restaurants partner with FoodExpress?
A: Restaurant owners can visit our website and fill partner registration form or call partner helpline at +91-7777777777. We'll contact within 24-48 hours for onboarding. Benefits include increased customer reach, marketing support, and analytics dashboard.

Q: What are peak hour surcharges?
A: During high demand periods like weekends, holidays, and meal times, surge pricing of Rs. 10-30 may apply to ensure delivery partner availability. This is clearly shown before checkout. FoodExpress Pro members are exempt from surge charges.

Q: How do you ensure food safety and hygiene?
A: All partner restaurants undergo hygiene verification and must maintain FSSAI food safety standards. We conduct regular audits and mystery checks. Customers can view restaurant hygiene ratings in app. Report hygiene concerns through app for immediate investigation.
"""

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# App header
st.title("🍔 FoodExpress FAQ Chatbot")
st.markdown("**Ask me anything about food ordering, delivery, payments, offers, and more!**")
st.markdown("---")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Use QA model to get answer
                result = qa_model(question=prompt, context=context)
                answer = result['answer']

                # Display answer
                st.markdown(answer)
                response = answer

            except Exception as e:
                error_msg = "I'm having trouble processing your question. Please try rephrasing it or contact our support team at +91-8888888888."
                st.markdown(error_msg)
                response = error_msg

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with example questions
with st.sidebar:
    st.header("📋 Example Questions")
    st.markdown("""
    Try asking:
    - What is your delivery time?
    - How do I place an order?
    - What payment methods do you accept?
    - How do I cancel my order?
    - Do you offer contactless delivery?
    - What are your delivery charges?
    - How do I track my order?
    - Can I modify my order?
    - What if my food quality is poor?
    - Do you have a membership program?
    """)

    st.markdown("---")
    st.markdown("**Support:** +91-8888888888")
    st.markdown("**Email:** support@foodexpress.com")
    st.markdown("**Available:** 24/7")

    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
