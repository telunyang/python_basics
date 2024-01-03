# 建立一個函式 price_a，回傳 100
def price_a():
    return 100

# 第一個是 function 物件，第二個是執行 function (回傳 100) 的結果
print(price_a)
print(price_a())

# 建立函式 price_b，作為 decorator，
# 收到函式物件，並在 price_b 執行該函式物件
def price_b(func):
    '''
    將 func (price_a) 執行後所回傳的值 (100)，
    乘上 1.2 後，再以暱名函式回傳
    '''
    return lambda: func() * 1.2

# 修飾子執行結果
myFunc = price_b(price_a)
print(myFunc())