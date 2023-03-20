# 自訂例外處理
x = -1

if x < 0:
    raise Exception("數字小於 0")



# 自訂型別錯誤的例外處理
x = "hello"

if type(x) is not int:
  raise TypeError("只接受整數型別")