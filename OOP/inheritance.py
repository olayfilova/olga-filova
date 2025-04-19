class Car:
    def __init__(self, wheel, color, hp):
        self.wheel = wheel
        self.color = color
        self.hp = hp

    def start(self):
        print(f"{self.__class__.__name__} starts ")

    def stop(self):
        print(f"{self.__class__.__name__} stops")

    # def drive(self):
    #
    #
    # def change_color(self, new_color):
    #     self.color = new_color


class Truck(Car):
    # def __init__(self):
        ...


class Plane:
    def fly(self):
        print("I can fly")


class FlyingTruck(Truck, Plane):
    ...


car = Car(4, "white", 100)
car.start()
car.stop()

t = Truck(4, "silv", 200)
t.start()
t.stop()

ft = FlyingTruck(4, "Blue", 800)
ft.start()
ft.fly()
ft.stop()
