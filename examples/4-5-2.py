# 建立字典
dict02 = {"name": "John", "age": 25, "city": "New York"}

# 透過items()方法取得字典的鍵值對
for t in dict02.items():
    print(t)
    print(f"key: {t[0]}, value: {t[1]}")
    print("=" * 50)