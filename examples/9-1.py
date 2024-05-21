# 匯入模組
import myModule

if __name__ == '__main__':
    # 計算幾次方
    num = myModule.pow(2, 3)
    print(num)

    # 簡單斷詞
    txt = "I will always love you"
    list_result = myModule.segment(txt)
    print(list_result)