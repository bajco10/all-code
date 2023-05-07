from car import Car
from car import ElectricCar as EC

my_new_car = Car("audi", "a4", 2018, "blue")
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_beetle = Car("volkswagen", "beetle", 2019, "grey")
print(my_beetle.get_descriptive_name())

my_tesla = EC("tesla", "roadster", 2019, "black")
print(my_tesla.get_descriptive_name())





