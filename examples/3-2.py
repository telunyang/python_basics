'''
while 迴圈
for 迴圈 
'''
# while 迴圈
count = 1
while count <= 5:
    print(count, end="")
    count = count + 1  # 或是寫成 count += 1



# for 迴圈 01
'''
用法
range(n, m-1)

說明
會走訪 n 到 m-1 的數字
'''
for i in range(5, 8):
    print(i, end = ",")



# for 迴圈 02
'''
用法
range(n, m-1, step)

說明
以每 step 為間距，走訪 n 到 m-1 的數字
'''
for i in range(5, 20, 2):
    print(i, end = ",")