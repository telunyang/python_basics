'''
格式化字串 - 使用 string.format()
'''
# 嵌入文字
msg = '{}, {}!'.format('Hello', 'World')
print(msg)

# 改變參數順序
msg = '{1}, {0}'.format('Hello', 'World')
print(msg)

# 指定寬度
msg = '[{:10}]'.format('Hello')
print(msg)

# 靠右對齊
msg = '[{:>10}]'.format('Hello')
print(msg)

# 靠左對齊
msg = '[{:<10}]'.format('Hello')
print(msg)

# 置中對齊
msg = '[{:^10}]'.format('Hello')
print(msg)

# 指定浮點數位數
msg = '[{:8.3f}]'.format(12.3456)
print(msg)

# 文字長度上限
msg = '[{:.3}]'.format('Hello')
print(msg)

# 空白補 0
msg = '[{:06.2f}]'.format(3.1415926)
print(msg)