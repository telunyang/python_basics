'''
生成圖像
https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw

適用語系
EN、es-MX、ja-JP、zh-CN、hi-IN
'''

import os
del os.environ["GOOGLE_API_KEY"]

from google import genai
from PIL import Image
from dotenv import load_dotenv
load_dotenv(override=True)

if "SSL_CERT_FILE" in os.environ:
    del os.environ["SSL_CERT_FILE"]

# 讀取 API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 建立 Client
client = genai.Client(api_key=GOOGLE_API_KEY)

# 你的 prompt
prompt = ('Hi, Can you add a cute car watermark next to the name "Darren"?',)

# 讀取圖片
image = Image.open('./example01.jpg')

# 取得回應
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt, image],
)

# 將回傳的圖片儲存並顯示出來
for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
        image.show()