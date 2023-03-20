'''區域變數無法修改全域變數'''
# 全域變數
name = "Bill"

# 定義函式
def set_name():
    # 區域變數
    name = "Doraemon"
    
# 執行函式
set_name()

# 輸出結果
print(name)



'''區域變數可以修改全域變數'''
# 全域變數
name = "Bill"

# 定義函式
def set_name():
    '''
    想在函式內部使用、修改外部變數的值，
    必須在變數前加上 global 關鍵字，
    但是不能在加上 global 的時候進行變數初始化 
    '''
    global name
    name = "Doraemon"
    
# 執行函式
set_name()

# 輸出結果
print(name)