class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())        

    def sub(self):
        self.append(self.pop() - self.pop())        

    def mul(self):
        self.append(self.pop() * self.pop())        

    def div(self):
        self.append(self.pop() // self.pop())        


def test():
    ex = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex.sum()

test()
