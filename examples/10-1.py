# 匯入 sys 模組
import sys

# 確認 argv 的內容
print(sys.argv)
'''
請在 Terminal 使用以下範例指令: 
python 10-1.py 100 3

輸出:
['10-1.py', '100', '3']
'''

# 簡單範例: 輸出 1 ~ 100 之間，3 的倍數
if len(sys.argv) < 3:
    print("參數量不足，至少需要 3 個參數。")
    print("使用方式: python 10-1.py <被除數> <除數>")

    '''
    sys.exit():
    中斷程式執行，直接結束程式，
    之後的程式碼不會繼續執行
    '''
    sys.exit() 

for i in range(1, int(sys.argv[1])):
    if i % int(sys.argv[2]) == 0:
        print(i, end=" ")