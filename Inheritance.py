class Animal:
    def speek(self):
        print("Animal is speeking...")

class Dog(Animal):
    def bark(self):
        print("Dog is barking...")

tommy = Dog()
tommy.bark()
tommy.speek()

a1 = Animal()
a1.speek()