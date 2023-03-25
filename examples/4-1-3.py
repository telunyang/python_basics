# f-string (又稱作 formatted string literals, version >= 3.6)
name = "Darren"
age = 18
result = f"name: {name}, age: {age}"
print(result)

# 靠左對齊、靠右對齊
result = f"name: [{name:<10}], age: [{age:>10}]"
print(result)

# 靠左對齊、靠右對齊，字數不足，補「ㄏ」(沒寫補什麼，預設空格)
result = f"name: [{name:ㄏ<10}], age: [{age:ㄏ>10}]"
print(result)

# 靠左對齊、靠右對齊，
result = f"name: [{name:^10}], age: [{age:^10}]"
print(result)

# 指定文字長度上限 (只有文字，才在格式化字串中加入「.」來限定字串長度)
result = f"name: [{name:^10.2}]"
print(result)