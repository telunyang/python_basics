import sys, os
from pprint import pprint

# 取得當前 python 版本所使用的環境變數
pprint(sys.path)

# 輸出當前工作/專案/教材目錄的絕對路徑
print(os.getcwd())

# 設定絕對/相對路徑，取得自訂模組
sys.path.insert(0, os.getcwd() + '\\examples')
from myModule import pow, segment

'''
補充範例

如果在 python_basics 的上一層目錄裡，新增 modules 資料夾，
新增一個 tools.txt 記事本檔案，將 myModule.py 裡面的內容複製到 tools.txt 裡面，
而且把 tools.txt 的副檔名改成 py。

最後將前面的程式碼改成以下的樣子：

sys.path.insert(0, '..\\modules')
from tools import pow, segment
'''

# 確認環境變數是否有新增
pprint(sys.path)

if __name__ == '__main__':
    # 計算幾次方
    num = pow(2, 3)
    print(num)

    # 簡單斷詞
    txt = "I will always love you"
    list_result = segment(txt)
    print(list_result)