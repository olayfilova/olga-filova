class A:
    def met(self):
        print("A")


class B(A):
    def met(self):
        print("B")
        super().met()

b=B()
b.met()


class Animal():
    def voice(self):
        print("Animal voice")


class Dog(Animal):
    def voice(self):
        print("Dog voice")


class Cat(Animal):
    def voice(self):
        print("Cat voice")