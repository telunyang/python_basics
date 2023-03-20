# 初始化 dict
dict01 = {"蘋果": 100, "橘子": 20, "水梨": 50}
print(dict01)

'''
也可以透過排版，寫成:

dict01 = {
    "蘋果": 100, 
    "橘子": 20, 
    "水梨": 50
}
'''

# 印出蘋果的價格
print(dict01["蘋果"])

# 修改橘子的價格
dict01["橘子"] = 30
print(dict01["橘子"])

# 刪除 水梨
del dict01["水梨"]
print(dict01)



'''
有時候會遇到比較複雜的結構，需要一層一層去走訪，取得資料
'''
dict02 = {
    'name': 'Darren',
    'age': 18,
    'info': {
        'nickname': 'boatman',
        'favorite_role': 'Doraemon',
        'phone_number': [
            '0911111111',
            '0922222222',
            '0933333333'
        ]
    }
}

# 取得 nickname
print( dict02['info']['nickname'] )

# 取得所有 phone_number
for number in dict02['info']['phone_number']:
    print(number)