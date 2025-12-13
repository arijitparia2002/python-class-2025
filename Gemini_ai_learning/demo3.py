from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

interaction =  client.interactions.create(
    model="gemini-2.5-flash",
    input="Tell me a short joke about programming."
)

print(interaction.outputs[-1].text)