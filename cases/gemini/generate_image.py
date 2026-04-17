'''
生成圖像
https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw

適用語系
EN、es-MX、ja-JP、zh-CN、hi-IN

需要繁體中文轉成英文，可以到:
https://translate.google.com.tw/?hl=zh-TW&sl=zh-TW&tl=en&op=translate
'''

import os

# (Optional) 刪除 SSL_CERT_FILE 環境變數，避免 SSL 錯誤
if "SSL_CERT_FILE" in os.environ:
    del os.environ["SSL_CERT_FILE"]

# (Optional) 刪除 GOOGLE_API_KEY 環境變數，因為有時候電腦會暫存舊的 API Key
if "GOOGLE_API_KEY" in os.environ:
    del os.environ["GOOGLE_API_KEY"]

from google import genai

# 讀取 .env 檔案中的環境變數
from dotenv import load_dotenv
load_dotenv(override=True)

# 讀取 API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 建立 Client
client = genai.Client(api_key=GOOGLE_API_KEY)

# 提示詞
prompt = ("Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme")

# 取得回應
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

# 將回傳的圖片顯示出來 (也會存檔)
for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
        image.show()