class FirstClass:
    def setdata(self, value):
        self.data = value
    
    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    
    def __add__(self, other):
        return ThirdClass(self.data + other)
    
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    
    def mul(self, other):
        self.data *= other


first = FirstClass()
first.setdata("aaa")
first.display()
second = SecondClass()
second.setdata(111)
second.display()

third = ThirdClass("abc")
third.display()
print(third)
third.mul(3)
print(third)
