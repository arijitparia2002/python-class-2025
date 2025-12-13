from google import genai
from config import GEMINI_API_KEY

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="What is the radius of the Earth?"
)
print(response.text)