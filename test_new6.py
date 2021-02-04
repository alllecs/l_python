class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        if self.money + v <= self.capacity:
            return True
        else:
            return False
    
    def add(self, v):
        self.money += v

a = MoneyBox(30)
a.add(15)
if a.can_add(10):
    a.add(10)
if a.can_add(5):
    a.add(5)
else:
    print(False)
