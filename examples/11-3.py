'''
使用 @ 語法的修飾子可以「由下往上」疊加，
將 @price_c 放到 @price_b 上方，
再執行、輸出 price_a() 的結果看看。
'''

# 建立函式 price_b (decorator)
def price_b(func):
    '''
    將 func (price_a) 執行後所回傳的值 (100)，
    乘上 1.2 後，再以暱名函式回傳
    '''
    return lambda: func() * 1.2

# 用來疊加的修飾子
def price_c(func):
    '''
    將 func (price_2) 執行後所回傳的值 (120)，
    乘上 2 後，再以暱名函式回傳
    '''
    return lambda: func() * 2

    # 除了暱稱函式外，常見還有以下寫法
    '''
    def tempFunc():
        return func() * 2
    return tempFunc
    '''

# python 以「@」作為修飾子符號
@price_c
@price_b
def price_a():
    return 100

# 修飾子執行結果
print(price_a())