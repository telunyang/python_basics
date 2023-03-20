# 建立一個家長類別
class Parent():
    def __init__(self):
        pass
    def post(self):
        return '發話中'
    
# 實體化 (instantiation)
obj_parent = Parent()
print(obj_parent.post())