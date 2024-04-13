from car import Car 
my_new_car = Car('Tata','Brilla', 2012, 'diesel') # importing a class 
print(my_new_car.diesel_car())

from car import Battery # importing another class
my_new_car = Battery('60','Brilla')
print(my_new_car.describe_battery())

from car import ElectricCar # importing a child class from a parent class
my_ev_car = ElectricCar('KKB', 'Beast', 2012, 'EV')
my_ev_car.describe_battery()

#importing multiple classes from a module
from car import Car, ElectricCar
my_new_car = Car('Tata','Brilla', 2012, 'diesel')
print(my_new_car.descriptive_name())

# giving aliases to the class
from car import Battery as Bt
my_new_car = Bt('60','Brilla')
print(my_new_car.describe_battery())

