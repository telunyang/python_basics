# 算術運算子
print(9 + 4)
print(3 / 2)
print(2 ** 3)



# 賦值運算子
a = 9
b = 4
a += b # 等於 a = a + b
print(a)
c = 3
d = 2
d **= c # 等於 d = d ** c
print(d)



# 比較運算子 (用 if 判斷)
e = 4
if e == 4:
    print('e 等於 4')
if e > 2:
    print('e 大於 2')
if e != 4:
    print('e 不等於 4')

# 如果程式區塊只需要執行 1 行程式碼，則可以這麼寫
if e == 4: print('e 等於 4') 



# 邏輯運算子
f = 8
name = 'Bill'
if f == 8 and name == 'Bill':
    print('ok')
if f == 6 or name == 'Bill':
    print('name 等於 Bill')



# 成員運算子
myList = [5, 5, 6, 6, 3, 3, 1, 2]
if 6 in myList:
    print('6 在 list 裡')
if 4 not in myList:
    print('4 不在 list 裡')