# 建立函式 price_b (decorator)
def price_b(func):
    '''
    將 func (price_a) 執行後所回傳的值 (100)，
    乘上 1.2 後，再以暱名函式回傳
    '''
    return lambda: func() * 1.2

# python 以「@」作為修飾子符號
@price_b
def price_a():
    return 100

# 修飾子執行結果
print(price_a())