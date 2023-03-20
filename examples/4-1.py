# 字串變數初始化
string01 = "1,2,3,4"
print(string01)


# 替換字串
'''
用法
string.replace(str1, str2)
說明
將 string 中的 str1 替換成 str2
'''
string02 = "Alex"
string02 = string02.replace('ex', 'len')
print(string02)


# 去除字串兩側空格
'''
用法
string.strip()
說明
去除字串 string 左、右兩邊的空格
'''
string03 = "        ___ccc___         "
print(string03)
print(string03.strip())


# 字串變成小寫或大寫
'''
用法
string.lower()
說明
將字串 string 裡的字母全部改成小寫
'''
print("CAR".lower())

'''
用法
string.upper()
說明
將字串 string 裡的字母全部改成大寫
'''
print("good".upper())