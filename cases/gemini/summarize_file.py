import os
from google import genai
from dotenv import load_dotenv
load_dotenv(override=True)

# 讀取 API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 建立 Client
client = genai.Client(api_key=GOOGLE_API_KEY)

# 上傳檔案
sample_doc = client.files.upload(file='./poem.txt')

# 提示詞
prompt = "對這個檔案進行摘要。"

# Generate content
response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[sample_doc, prompt]
)
print(response.text)