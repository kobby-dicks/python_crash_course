"""A model of a car"""
class Car:
    """making a new car"""
    def __init__(self, brand, model, year, engine_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_type = engine_type

    def descriptive_name(self):
        long_name = (
        f'{self.brand}, {self.model}, {self.year}, {self.engine_type}'
        )
        return long_name.title()

    def diesel_car(self):
        self.engine_type = 'Diesel'
        print(f'My first car has a {self.engine_type} engine.')

class Battery:
    """making a new battery"""
    def __init__(self, battery_size, battery_type):
        self.battery_size = battery_size
        self.battery_type = battery_type
    def describe_battery(self):
        print(f'My second car has a {self.battery_size} kWh battery.')
        print(f'This car has a {self.battery_type} battery.')

class ElectricCar(Car):
    def __init__(self, brand, model, year, engine_type):
        super().__init__(brand, model, year, engine_type)
        self.battery = Battery(100, 'Lithium')
        self.num_of_cylinders = 4
        self.odometer_reading = 400

    def describe_battery(self):
        print(f'My second car is a {self.engine_type} car')
        print(f'This car has a {self.battery.battery_size} kWh battery.')
        print(f'This car has a {self.battery.battery_type} battery.')
        print(f'This car has {self.num_of_cylinders} cylinders.')
        print(f'This car has {self.odometer_reading} miles on it.')
        print(f'This car has a {self.engine_type} engine.')

My_latest_car = Battery('50', 'Lithium')
print(My_latest_car.describe_battery())

my_first_car = Car('Tata', 'Samira', 2019, 'diesel')
print(my_first_car.diesel_car())