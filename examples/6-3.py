# 建立家長類別
class Parent():
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    def post(self):
        return '發話中'

# 建立子類別
class Child(Parent):
    '''
    這裡的 __init__ 屬於 Child 類別的，會將 Parent 的 __init__ 覆蓋掉
    '''
    def __init__(self, height, weight):
        # 這裡將 Parent 所有屬性、方法繼承下來
        super().__init__(height, weight)
        self.height = height
        self.weight = weight
    def reply(self):
        return '回話中'
    def content(self):
        return '我知道了'

# 實體化 Parent 物件
obj_parent = Parent(165, 80)
print(obj_parent.height)
print(obj_parent.weight)
print(obj_parent.post())

# 實體化 Child 物件
obj_child = Child(172, 95)
print(obj_child.height)
print(obj_child.weight)
print(obj_child.post())
print(obj_child.reply())
print(obj_child.content())