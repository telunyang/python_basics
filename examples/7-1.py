# 可以連續定義數個例外處理機制，最符合的例外事件類別會先拋出
try:
    print(x)
except NameError:
    print("x 尚未宣告")
except:
    print("某個東西出錯了")



# 多層例外處理: 內部的例外處理會優先補捉，捕捉不到，才會由在外部的例外處理來補捉
try:
    try:
        print(y)
    except NameError as err:
        print("NameError:")
        print(str(err))
except Exception as err:
    print("Exception:")
    print(str(err))



# 如果沒有錯誤，就會執行 else 程式區塊，finally 程式區塊是無論有無錯誤，都會執行
try:
    z = 5
    print(z)
except NameError:
    print("變數尚未宣告")
else:
    print('沒有例外發生')
finally:
    print('程式結束')