'''
ZIP 檔案解壓縮

需要下載範例檔案，請先安裝 wget
$ pip install wget

參考資料
[1] Python 使用 zipfile 模組壓縮、解壓縮 ZIP 檔案教學與範例
https://officeguide.cc/python-zipfile-module-compression-decompression-tutorial-examples/
'''

import os, zipfile, wget

# zip 檔案若是不存在
if not os.path.exists("./f-instrument01.zip"):
    # 下載 zip
    wget.download('https://www.dropbox.com/s/0cm2vqmnbasz32t/f-instrument01.zip?dl=1')


# 存放路徑 (將解壓縮的內容另存到這裡)
path_folder = './files'

# 確認 資料夾是否存在
if not os.path.exists(path_folder):
    # 建立資料夾
    os.makedirs(path_folder)

try:
    # 對 zip 檔案解壓縮 至 指定路徑
    with zipfile.ZipFile("./f-instrument01.zip", 'r') as zf:
        # 檢視 zip 檔案內容 (zf.namelist()[0] 通常是放置檔案的資料夾)
        print(zf.namelist())

        # 解壓縮
        zf.extractall(path = path_folder)
except Exception as err:
    print('zip 無法開啟')
    print(err)
else:
    print('zip 解壓縮成功')