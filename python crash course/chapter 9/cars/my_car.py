from car import Car as C
from electric_car import ElectricCar as EC
from battery import *		


my_beetle = C('volkswagen','beetle',2019)
print(f"\n{my_beetle.get_descriptive_name()}")
my_beetle.update_odometer(23_500)
my_beetle.read_odometer()


my_tesla = EC('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()