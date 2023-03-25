'''
下載 google 小姐的聲音
'''
# 子程序
import subprocess

# 將人類可讀的文字，轉換成瀏覽器可讀的網址格式
from urllib.parse import quote


'''
測試單句下載 mp3
'''
# 設定給 google 小姐發音的文字
words = '我的優點就是帥，缺點就是帥得不明顯'

# 轉成符合 url 格式的文字
encode_url = quote(words)

# 定義指令
cmd = [
    'curl', 
    '-X', 
    'GET', 
    f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encode_url}',
    '-o',
    f'./{words}.mp3'
]

# 執行指令，回傳 Process 物件，其中的屬性 returncode == 0 代表成功
std_output = subprocess.run(cmd)
if std_output.returncode == 0:
    print(f'[{words}] 下載成功')
else:
    print(f'[{words}] 下載失敗')




'''
多句下載
'''
# 設定多個給 google 小姐發音的句子
list_words = [
    '人生短短幾個秋啊',
    '不醉不罷休',
    '東邊我的美人哪',
    '西邊黃河流'
]

# 把每一句都下載成 mp3
for words in list_words:
    # 轉成符合 url 格式的文字
    encode_url = quote(words)

    # 定義指令
    cmd = [
        'curl', 
        '-X', 
        'GET', 
        f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encode_url}',
        '-o',
        f'./{words}.mp3'
    ]

    # 執行指令，回傳 Process 物件，其中的屬性 returncode == 0 代表成功
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'[{words}] 下載成功')
    else:
        print(f'[{words}] 下載失敗')