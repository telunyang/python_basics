# 初始化一個字串
myStr = 'Hello,World!'


'''
透過冒號（:）進行分割
'''
# 從頭取到 5（不包含第 5 個元素，實際為 0 ~ 4）
print( myStr[0:5] ) # 索引從 0 開始，到 5 - 1 的索引位置

# 從頭取到 5（不包含第 5 個元素，實際為 0 ~ 4）
print( myStr[:5] ) # 冒號前面留空，效果跟 [0:5] 一樣

# 從 7 取到尾
print( myStr[7:] )  # 冒號後面留空

# 從 7 取到 9（不包含第 9 個元素，實際為 7 ~ 8）
print( myStr[7:9] )



'''
使用負號
'''
# 從倒數第 10 取到倒數第 7（不包含倒數第 7 的元素）
print( myStr[-10:-7] )

# 從倒數第 5 取到尾
print( myStr[-5:] )

# 從頭取到倒數第 7（不包含倒數第 7 的元素）
print( myStr[:-7] )



# 取得檔案全名
string06 = "/home/darren/ebook.txt"
list06 = string06.split("/")
print(list06[-1])



# 搜尋字串
string07 = 'believe'
result07 = string07.find('lie')
'''
用法
string.find(str)
說明
回傳 string 第一次在字串 string 中出現的 index，若找不到則回傳 -1
'''
print(result07)