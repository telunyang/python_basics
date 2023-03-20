# 刪除檔案
import os # 匯入套件

# 檔案路徑
file_path = './8-2.txt'

# 如果指定路徑的檔案存在，則進行刪除
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('Not found')