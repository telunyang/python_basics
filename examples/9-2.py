# 直接從模組中匯入函式
from myModule import pow, segmentSentence

# 計算幾次方
num = pow(2, 3)
print(num)

# 簡單斷句
txt = "I will always love you"
list_result = segmentSentence(txt)
print(list_result)