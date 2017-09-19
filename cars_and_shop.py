class Car:
    def __init__(self, name, color, price, year):

        self.name = name
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.name, self.color, self.price, self.year)

class Showroom:

    def __init__(self, address, name):
        self.address = address
        self.name = name
        self.cars = []


    def add_car(self, Car):
        self.cars.append(Car)

    def show_all(self):
        a =1
        for i in self.cars:
            print(a)
            print('_____________________________')
            print(i)
            a =a +1
    def sell_car(self, car):
        if car  in self.cars:
            self.cars.remove(car)
            print('Car has been sold!')
        else:
            print('No such car')







room = Showroom('Kyiv', 'Supercar')
car1 = Car('subaru', 'pink', 60000, 2017)
car2 = Car('mustang', 'yellow', 80000, 2014)
room.add_car(car1)
room.add_car(car2)
room.sell_car(car1)
room.show_all()
