'''
條件判斷
if ... else; if ... elif ... else; True 和 False
'''

# if
num = 10
'''
可以用以下符號來進行條件判斷
== (等於)
> (大於)
>= (大於等於)
< (小於)
<= (小於等於)
!= (不等於)
'''
if num > 5:
    print("num 大於 5")

# if else
name = 'apple'
if name == 'apple':
    print('名稱是 apple')
else:
    print("名稱不是 apple")

# if elif else
name = 'darren'
if name == "alex":
    print("名稱: alex")
elif name == "bill":
    print("名稱: bill")
elif name == "carl":
    print("名稱: carl")
else:
    print("Not found")

# 補充: True (真) 和 False (假、偽)
is_available = True
if is_available == True:
    print("真")
else:
    print("假")

# 也可以不用加「 == True」
if is_available:
    print("真")
else:
    print("假")