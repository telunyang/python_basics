'''
威力彩
https://www.taiwanlottery.com.tw/Superlotto638/index.asp

規則:
威力彩是一種樂透型遊戲，其選號分為兩區，
您必須從第1個選號區中的 01 ~ 38 的號碼中任選6個號碼，
並從第2個選號區中的 01 ~ 08 的號碼中任選 1 個號碼進行投注，
這 六個 + 一個 號碼即為您的投注號碼。


參考網址:
[1] Python 随机数生成
https://www.runoob.com/python3/python3-func-number-random.html
[2] Python math 模块
https://www.runoob.com/python3/python-math.html
[3] Python random randint() 方法
https://www.runoob.com/python3/ref-random-randint.html
'''


'''匯入套件(模組)'''
import random, math
# 

# 放置第一選號區 6 個號碼的變數
set_01 = set()

# 放置第二選號區的 1 個號碼的變數
num_02 = None

# 取得 1 ~ x 之間的值
def get_random_num(x):
    '''
    假設 x 為 38，
    「random.random() * x」產生的值就落在 0.00... - 37.99... 之間，
    透過 math.floor() 取得無條件捨去，此時程式後面再加 1，代表產生的值落在 1 - 38 之間，
    最後進行回傳
    '''
    return math.floor( random.random() * x ) + 1


# 暴力法
while True:
    # 先取得第一選號區的六個號碼
    num_01 = get_random_num(38)

    # 如果第一選號區不足六個號碼，同時號碼也不曾在第一選號區出現過，則加入 set
    if len(set_01) < 6:
        set_01.add(num_01)
    else:
        # 為第二選號區加入一個號碼
        num_02 = get_random_num(8)

        # 離開 while 迴圈
        break

# 有關 sorted 可參考: https://www.w3schools.com/python/ref_func_sorted.asp
print('第一選號區: ', sorted(list(set_01), reverse=False))
print('第二選號區: ', num_02)

'''
如果
把 num_01 = get_random_num(38) 改成 num_01 = random.randint(1, 38)
把 num_02 = get_random_num(8) 改成 num_02 = random.randint(1, 8)
結果會是如何呢?
'''