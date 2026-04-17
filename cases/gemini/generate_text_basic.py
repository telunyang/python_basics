import os
from google import genai
from dotenv import load_dotenv
load_dotenv(override=True)

# 讀取 API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 建立 Client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Generate content
response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=["請簡單地解釋 AI 是如何運作的，只要 100 個字。"]
)
print(response.text)