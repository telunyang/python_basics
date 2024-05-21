# 自訂例外處理
x = -1

try:
    if x < 0:
        raise Exception("數字小於 0")
except Exception as e:
    # 可以在這裡加入處理錯誤的程式碼，例如 logging 機制
	print(e)


# 自訂型別錯誤的例外處理
x = "hello"

try:
    if type(x) is not int:
        raise TypeError("只接受整數型別")
except TypeError as e:
    # 自訂處理錯誤的程式碼
	print(e)