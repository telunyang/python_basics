from google import genai
import os
import pprint
from dotenv import load_dotenv
load_dotenv(override=True)

# 讀取 API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 建立 Client
client = genai.Client(api_key=GOOGLE_API_KEY)

# 列出所有模型
for model in client.models.list():
    # 所有模型資訊
    print("-" * 50)
    pprint.pprint(model)

    # 篩選出 Gemma 模型
    # if "gemma" in model.name.lower():
    #     print("-" * 50)
    #     pprint.pprint(model)
        