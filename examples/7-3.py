import logging

'''
Logging 設定
'''
# 基本設定
logger = logging.getLogger('my_app')

# 設定等級
logger.setLevel(logging.INFO)

# 設定輸出格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")

# 儲存在 log 當中的事件處理器
fileHandler = logging.FileHandler('my_app.log', mode='a', encoding='utf-8') # a: append, w: write
fileHandler.setFormatter(formatter)

# 輸出在終端機介面上的事件處理器
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 加入事件
logger.addHandler(console_handler)
logger.addHandler(fileHandler)



# 基本範例
for x in range(0, 11):
    if x > 5:
        logger.warning(f"數字 {x} 大於 5")
    else:
        logger.info(f"數字 {x} 在合理範例")

# 整合 try - except 機制 (非正式)
for x in range(0, 11):
    try:
        if x > 5:
            raise Exception(f"數字 {x} 大於 5")
        else:
            logger.info(f"數字 {x} 在合理範例")
    except Exception as err:
        logger.warning(err)