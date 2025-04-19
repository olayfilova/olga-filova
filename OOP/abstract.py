from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        raise NotImplementedError("Subclasses must implement move method")


# v=Vehicle().  ###conceptualy, not work abs from abs
# print(v.move())


class Boat(Vehicle):
    def move(self):
        print("Boat is moving")

class Car(Vehicle):
    def move(self):
        print("Car is moving")


b=Boat()
print(b.move())

c = Car()
print(c.move())