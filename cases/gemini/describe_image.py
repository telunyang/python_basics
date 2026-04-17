'''
參考結果
https://i.imgur.com/o6QvMn9.png
'''

import os
from PIL import Image
from google import genai
from dotenv import load_dotenv
load_dotenv(override=True)

# 讀取 API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 建立 Client
client = genai.Client(api_key=GOOGLE_API_KEY)

# 讀取圖片
image = Image.open("./example01.jpg")

# 進行圖片描述
response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[image, "請形容這張圖片的內容，其中有一個物件上面寫著字，請問上面寫什麼？"]
)
print(response.text)