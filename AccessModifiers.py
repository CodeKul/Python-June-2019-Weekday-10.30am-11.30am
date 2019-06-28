class MyClass:
    a = 0
    _b = 0
    __c = 0

    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c
    
    def __display(self):
        print(self.__c)

    def display(self):
        self.__display()


obj = MyClass(10, 20, 30)
obj.a = 30
print(obj.a)

obj._b = 50
print(obj._b)
        
obj.__c = 70
print(obj.__c)

obj._MyClass__display()

obj.__init__(1,2,3)
