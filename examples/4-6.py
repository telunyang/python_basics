# Set 初始化: 第一種
mySet01 = {"網路", "爬蟲", "真好玩"}
print(mySet01)

# Set 初始化: 第二種 (裡面放 tuple)
mySet02 = set( ("網路", "爬蟲", "真好玩") )
print(mySet02)

# 一筆筆讀資料 : for 迴圈
for data in mySet02: 
    print(data)

# 總共有幾筆資料: len()
print( len(mySet02) )

# 因為沒有序號、索引的概念，所以無法透過指定索引輸出
print( mySet01[0] )

# 添加一筆資料: add()
mySet01.add("嗎?")
mySet02.add("對不對?")

print(mySet01)
print(mySet02)

# 此時新增重複的，資料不會增加
mySet01.add("真好玩")
print(mySet01)

# 添加多筆資料: update()
mySet01.update(["甲", "乙", "丙"])
mySet02.update(["子", "丑", "寅"])
print(mySet01)
print(mySet02)

# 查詢陣列中有沒有我要的資料: in (只回傳 true 或 false)
print( "甲" in mySet01 )
print( "甲" in mySet02 )

if "乙" in mySet01:
    print("有資料")
else:
    print("找不到資料")

# 刪除元素: discard() or remove()
mySet01.discard("丙")
print(mySet01)
mySet02.remove("丑")
print(mySet02)

# 清空: clear()、del
'''.clear() 會清空 set 變數，但變數依然存在，所以會印出空 set'''
mySet01.clear()
print(mySet01)
''' del 會將 set 變數從記憶體中刪除，所以刪除完後，變數會變成未宣告的狀態'''
del mySet02
print(mySet02)