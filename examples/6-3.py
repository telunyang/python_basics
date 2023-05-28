# 建立家長類別
class Parent():
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.money = 100000000
    def post(self):
        return '發話中'

# 建立子類別
class Child(Parent):
    '''
    這裡的 __init__ 屬於 Child 類別的，會將 Parent 的 __init__ 覆蓋掉
    '''
    def __init__(self, height, weight):
        '''
        super() 代表父類別，
        super().__init__() 代表使用父類別的建構子，
        在執行這行程式碼時，會自動將 Parent 所有屬性、方法繼承下來
        (包括 self.money)
        '''
        super().__init__(height, weight)
        self.height = height
        self.weight = weight
    def reply(self):
        return '回話中'
    def content(self):
        return '我知道了'
    def post(self): # overwrite (覆寫) 父類別的方法
        return '不要再發話了'

# 實體化 Parent 物件
obj_parent = Parent(165, 80)
print(obj_parent.height)
print(obj_parent.weight)
print(obj_parent.post())

# 實體化 Child 物件
# (此時 Child 除了自己的屬性、方法外，還擁有父類別的屬性、方法)
obj_child = Child(172, 95)
print(obj_child.height)
print(obj_child.weight)
print(obj_child.money)
print(obj_child.reply())
print(obj_child.content())
print(obj_child.post())