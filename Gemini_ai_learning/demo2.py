import google.generativeai as genai
from config import GEMINI_API_KEY


# Configure API
genai.configure(api_key=GEMINI_API_KEY)
# Create model
model = genai.GenerativeModel('gemini-2.5-flash')
# Generate response
response = model.generate_content("What is Python programming?")
# Print response
print(response.text)