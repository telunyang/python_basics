from dotenv import load_dotenv, dotenv_values
import os

# 讀取 .env 檔案 (使用 load_dotenv)
load_dotenv() 

# 取得 .env 檔案內容 (內容的變數名稱可以是小寫，也可以是大寫)
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
print(username, password)

# 讀取 .env 檔案 (使用 dotenv_values)
config = dotenv_values(".env")

# 取得 .env 檔案內容 (內容的變數名稱可以是小寫，也可以是大寫)
print(config) # config = {'USERNAME': 'darren', 'PASSWORD': 123456}
print(config['USERNAME'], config['PASSWORD'])