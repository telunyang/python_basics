# Tuple 初始化: 第一種
myTuple01 = ("人", "帥", "得體")
print(myTuple01)
print(type(myTuple01))

# Tuple 初始化: 第二種
myTuple02 = "哆", "啦", "A", "夢"
print(myTuple02)
print(type(myTuple02))

# 透過指定索引輸出值
print( myTuple01[1] )
print( myTuple02[1] )

# 複數變數修改值
a = 10
b = 20
print("交換前: a = {}, b = {}".format(a, b))
a, b = b, a
print("交換後: a = {}, b = {}".format(a, b))

# list 可以修改指定索引的值
myList = ["人", "帥", "任性"]
myList[2] = "真好"
print(myList)

# tuple 不可以修改指定索引的值
myTuple = ("人", "帥", "任性")
myTuple[2] = "真好"
print(myTuple)

# 新增資料到 tuple (類似合併的方式)
myTuple01 = myTuple01 + ("哈",) # 只加入 1 個字
print(myTuple01)
myTuple01 = myTuple01 + ("哈", "哈") # 2 個字以上，最後一個元素不用加「,」
print(myTuple01)

# tuple 之間可用 + 來合併
myTuple03 = myTuple01 + myTuple02
print(myTuple03)

# 用 for 迴圈逐一輸出資料
for value in myTuple01:
    print(value)

# 用 len 計算 tuple 資料個數
print( len(myTuple02) )

# 因為無法修改 tuple 的資料，所以也無法指定索引進行刪除
del myTuple01[1]
print(myTuple01)

# 只能從記憶體刪除整個 tuple 變數
del myTuple01
print(myTuple01)