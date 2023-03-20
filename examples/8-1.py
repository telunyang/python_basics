# 讀取檔案內容 - 舊的寫法
f = open(file="./2-1.py", mode="r", encoding="utf-8")
print( f.read() )
f.close() # 關閉檔案，否則執行期間，在關閉前，會變成唯讀狀態

# 印出 50 個 等號
print("=" * 50)

# 讀取檔案內容 - 現今常用的寫法 (執行完畢會自動關閉檔案)
with open(file="./2-1.py", mode="r", encoding="utf-8") as f:
    print( f.read() )

# 印出 50 個 等號
print("=" * 50)

# 一行一行讀出來
with open(file="./2-1.py", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line) # 每一行後面會用 \n 結尾，所以輸出會有多次斷行的效果