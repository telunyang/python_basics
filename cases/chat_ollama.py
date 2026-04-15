'''
Ollama
https://ollama.com/

Ollama Python SDK
https://github.com/ollama/ollama-python
'''
# 測試 ollama 遠端連線
import requests

url = "http://localhost:11434/api/tags"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Ollama connection successful.")
    else:
        print(f"Failed to connect to Ollama. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error connecting to Ollama: {e}")


# 測試 ollama 聊天功能
'''
import asyncio
from ollama import AsyncClient
import time

messages = [
    {
        'role': 'user', 
        'content': '幸福的定義是什麼？簡單說明。'
    },
]

async def chat():
    t1 = time.time()
    response = await AsyncClient(
        host='http://localhost:11434',
        timeout=600
    ).chat(
        model='gemma4:e2b', 
        messages=messages,
        keep_alive="1h"
    )
    print(response.message.content)
    t2 = time.time()
    print(f"Response time: {t2 - t1:.2f} seconds")

asyncio.run(chat())
'''

# 測試 ollama 聊天功能 (streaming)
'''
import asyncio
from ollama import AsyncClient
import time

messages = [
    {
        'role': 'user', 
        'content': '幸福的定義是什麼？簡單說明。'
    },
]

async def chat():
    t1 = time.time()
    async for part in await AsyncClient(
        host='http://localhost:11434',
        timeout=600
    ).chat(
        model='gemma4:e2b', 
        messages=messages,
        keep_alive="1h",
        stream=True
    ):
        print(part['message']['content'], end='', flush=True)
    t2 = time.time()
    print(f"\nResponse time: {t2 - t1:.2f} seconds")

asyncio.run(chat())
'''