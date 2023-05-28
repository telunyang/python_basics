# 建立一個家長類別
class Parent():
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.money = 100000000
    def post(self):
        return '發話中'
    
# 實體化 (instantiation)
obj_parent = Parent(165, 80)
print(obj_parent.height)
print(obj_parent.weight)
print(obj_parent.money)
print(obj_parent.post())