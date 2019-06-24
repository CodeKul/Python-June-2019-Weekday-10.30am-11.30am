class MyClass:
    a = 0
    b = 0

    # def __init__(self):
    #     self.a = 0
    #     print('__init__')

    # def __init__ (self, a, b):
    #     self.a = a
    #     print('__init__ with param')

    def __init__(self, obj=None):
        if obj == None:
            self.a = 0
            self.b = 0
        else:
            self.a = obj.a
            self.b = obj.b

    def display(self):
        print('Value of a:',self.a)
        print('Value of b:',self.b)

obj1 = MyClass()
obj1.a = 30
obj1.b = 100
print('Object 1:')
obj1.display()

obj2 = MyClass(obj1)
print('Object 2:')
obj2.display()