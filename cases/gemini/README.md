# 透過 Google AI 的 API，來使用 Gemini 模型
- [Gemini API 文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

## Google AI Studio
申請 API Key [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### 使用 Google Gen AI Python SDK
使用套件 [https://github.com/googleapis/python-genai](https://github.com/googleapis/python-genai)

### 套件安裝
`pip install -r requirements.txt`

### 說明
- 將 `.env.example` 複製一份並命名為 `.env`
- 申請完 API，請將 API Key 存放在 `.env` 檔案中，並命名為 `GOOGLE_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`

### Gemini 模型
- [模型列表](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)
- [使用 Gemini API 執行 Gemma](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api?hl=zh-tw)