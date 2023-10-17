# 文字內容
text = '''人生短短幾個秋啊
不醉不罷休
東邊我的美人哪
'''

# 寫入檔案
with open("./8-2.txt", "w", encoding="utf-8") as f:
    f.write(text)

# 寫入最後一行 (附加文字在檔案內容最後一行)
with open("./8-2.txt", "a", encoding="utf-8") as f:
    f.write("西邊黃河流" + "\n")