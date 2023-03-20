# 文字內容
text = '''教我撩妹
你長得很像我的一個朋友
像誰
'''

# 寫入檔案
with open("./8-2.txt", "w", encoding="utf-8") as f:
    f.write(text)

# 寫入最後一行 (附加文字在檔案內容最後一行)
with open("./8-2.txt", "a", encoding="utf-8") as f:
    f.write("你長得很像我下一任女朋友")