'''不回傳 值'''

# 定義函式
def show_name():
    print("Doraemon")
    
# 執行函式
show_name()



'''回傳 值'''

# 定義函式
def get_name():
    name = "Doraemon"
    return name
    # 也可以寫成 return "Doraemon"
    
# 執行函式
result = get_name()

# 輸出回傳結果
print(result)



'''傳遞變數'''

# 定義函式
def get_greeting(name):
    return "Hello, " + name

# 執行函式
result = get_greeting("Darren")

# 輸出回傳結果
print(result)