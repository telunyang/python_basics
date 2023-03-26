# 帶入參數，並將計算結果直接回傳
add = lambda x, y : x * y
print( add(3, 5) )

# 回傳之前的條件判斷 (需要練習一下語法，否則一開始不好理解)
abs = lambda x : x if x >= 0 else -x
print( abs(5) )
print( abs(-5) )

# 不使用變數當作函式名稱，直接執行
print( (lambda x,y : x * y)(4, 5) )

# 與 map 函式一起使用
list_map = list(map(lambda x : x ** 2, [1, 2, 3, 4, 5])) 
print(list_map)

# 與 sorted 函式一起使用
myList = [
    {"name": "Alex", "age": 18},
    {"name": "Bill", "age": 25},
    {"name": "Carl", "age": 21},
    {"name": "Darren", "age": 10},
]
list_sorted = sorted(myList, key=lambda d: d['age'], reverse=False)
print(list_sorted)