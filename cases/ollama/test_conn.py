'''
Ollama
https://ollama.com/

Download for Windows
https://ollama.com/download/OllamaSetup.exe

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
