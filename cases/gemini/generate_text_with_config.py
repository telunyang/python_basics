import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

# 讀取 API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 建立 Client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Generate content
response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=["請簡單地解釋 AI 是如何運作的，只要 100 個字。"],
    config=types.GenerateContentConfig(
        system_instruction="你是一個知識淵博且樂於助人的 AI 助理。",
        temperature=0.1,
        top_p=0.95,
        top_k=50,
        candidate_count=1,
        seed=42,
        max_output_tokens=500,
        stop_sequences=['STOP!'],
        presence_penalty=0.0,
        frequency_penalty=0.0,
        # thinking_config=types.ThinkingConfig(thinking_level="low") 
    )
)
print(response.text)

'''
presence_penalty

這個參數關注的是 「話題的新鮮度」。
機制： 只要一個詞在已經生成的文本中出現過一次，AI 就會受到懲罰，增加它選擇「全新詞彙」的機率。
數值高 (例如 1.0)： AI 會更傾向於談論不同的話題或引入新的概念，適合激發創意或發散性思考。
數值低 (例如 0.0)： AI 會專注於當前的上下文，不會刻意避開已經提過的詞彙。
核心目標是「引入新話題」，有點像是對 AI 說：「別老是繞著這幾個點轉，講點別的！」、「換個話題吧！」

-----------------

frequency_penalty

這個參數關注的是 「詞彙的累積次數」。
機制： 一個詞出現的次數越多，懲罰就越重。這是一種遞增式的打壓。
數值高 (例如 1.0)： 極力避免重複使用相同的字眼。如果 AI 剛說過「漂亮」，下次它可能會被迫改說「美麗」或「迷人」。
數值低 (例如 0.0)： 允許 AI 正常重複常用詞彙（如「的」、「是」或是專業術語）。
核心目標是「減少字眼重複」，有點像是對 AI 說：「這個字你剛才講三遍了，換個詞說！」、「別老是用同一個詞！」

-----------------

什麼時候該調整它們？

當 AI 陷入死循環： 如果你發現 AI 一直重複同一句話（Looping），稍微調高這兩個數值（例如設為 0.1 到 0.5）通常能打破循環。
寫詩或創意寫作： 調高它們可以讓 AI 詞彙更豐富、不囉唆。
技術文檔或法律翻譯： 建議保持 0.0。因為專業術語必須精準重複，如果強迫 AI 換詞，反而會造成誤解。

-----------------

小提醒：

在目前的程式碼中，temperature 設為 0.1 已經讓 AI 非常保守且穩定了。
如果在此基礎上再大幅調高 Penalty，有時候會讓 AI 為了「避開重複」而開始胡言亂語（因為它被迫選一個機率極低、甚至不相關的字）。
如果設定 temperature 較高（例如 0.7 以上），再調高 Penalty 效果會比較好，因為 AI 本來就有較高的隨機性，不會那麼容易陷入死循環。
不過這些都是經驗法則，實際效果還是要多測試、多微調，才能找到最適合你應用場景的參數組合。
'''

'''
thinking_config=types.ThinkingConfig(thinking_level="low")

設定思考層級為「低」，代表 AI 將進行基本的推理和分析，適合處理簡單的任務和問題。
設定思考層級為「高」，代表 AI 將進行更深入和複雜的推理，適合處理需要多步驟思考或更複雜邏輯的任務。
注意！要 Gemini 3 系列才支援思考模式。
請參閱 https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw#thinking-levels
'''