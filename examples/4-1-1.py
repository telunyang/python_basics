'''
格式化字串 - 使用 %
'''
# 多組文字
msg = '%s, %s!' % ('Hello', 'World')
print(msg)

# 整數
msg = 'I am %d years old.' % 5
print(msg)

# 文字與整數
msg = '%s is %d years old.' % ('Alex', 18)
print(msg)

# 指定寬度 (維持 10 個字元長度，預設向右對齊)
msg = '[%10s]' % 'Hello'
print(msg)

# 靠左對齊 (維持 10 個字元長度，向左對齊)
msg = '[%-10s]' % 'Hello'
print(msg)

# 指定浮點數位數
msg = '[%8.3f]' % 12.3456
print(msg)

# 文字長度上限
msg = '[%.3s]' % 'Hello'
print(msg)

# 空白補 0
msg = '[%06.2f]' % 3.1415926
print(msg)