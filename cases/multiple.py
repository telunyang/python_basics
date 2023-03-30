'''
在限定範圍內，只印出某個數字的倍數
'''

# 印出 3 的倍數
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")

# 印出 50 個 = 號
print("=" * 50)

# 印出 2 跟 3 的公倍數
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")