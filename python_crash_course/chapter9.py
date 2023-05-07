
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog stitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    
    def describe_restaurant(self):
        print(f"\n{self.restaurant_name.title()} serves {self.cuisine_type} cuisine and served {self.number_served} cuntomers.")


    def open_restaurant(self, open, closed):
        print(f"The restaurant is open {open} - {closed}.")

    def set_number_served(self, number_of_customers):
        self.number_served = number_of_customers
    
    def increment_number_served(self, increment_of_customers):
        self.number_served += increment_of_customers
    
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "pistacio", "nuts", "tutti-frutti"]

    def get_flavors(self):
        for flavor in self.flavors:
            print(flavor)

new_stand = IceCreamStand("podhaj", "ice cream")
new_stand.describe_restaurant()
new_stand.get_flavors()



restaurant = Restaurant("pizza pub Orea", "Italian")
restaurant.set_number_served(100)
restaurant.increment_number_served(50)
restaurant.describe_restaurant()
restaurant.open_restaurant(6, 18)

 
restaurant1 = Restaurant("harley", "steak based")
restaurant1.describe_restaurant()
restaurant1.open_restaurant(12, 2)

restaurant2 = Restaurant("chinese restaurant", "chinese")
restaurant2.describe_restaurant()
restaurant2.open_restaurant(8, 22)

class User:
    def __init__(self, first_name, last_name, age, city, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.occupation = occupation
        self.login_attempts = 0
        
    
    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()} is {self.age}, lives in {self.city.title()} and is a {self.occupation}.")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, city, occupation):
        super().__init__(first_name, last_name, age, city, occupation)
    
class Privilidges:
    def __init__(self):
        self.priviliges = [
            "can add post", "can delete post", "can ban user", "can change password", "can skip the queue"
        ]
    
    def show_priviliges(self):
        print("These are your privilidges: ")
        for privilidge in self.priviliges:
            print(privilidge)


p1 = User("John", "Johnson", 27, "LA", "CEO of life")
p1.describe_user()
p1.greet_user()
p1.increment_login_attempts()
p1.increment_login_attempts()
p1.increment_login_attempts()
p1.increment_login_attempts()
p1.increment_login_attempts()
print(p1.login_attempts)
p1.reset_login_attempts()
print(p1.login_attempts)

p2 = User("Elon", "Musk", 44, "new york", "CEO of Tesla")
p2.describe_user()
p2.greet_user()

p3 = User("Jozo", "Raz", 59, "trnava ", "frontman of Elán")
p3.describe_user()
p3.greet_user()

a1 = Admin("Majo", "Vajo", 18, "Sučany", "maliar mostov")
a1.describe_user()
a1.greet_user()
a1 = Privilidges()
a1.show_priviliges()



class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year, color):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.color = color

    def get_descriptive_name(self):
        """Return a nearly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model} {self.color}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print(f"The gas tank on {self.make} {self.model} is filled!")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, color):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year, color)
        self.battery = Battery() 
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_batery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100


my_tesla = ElectricCar("tesla", "model s", 2019, "red")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_batery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_batery()
my_tesla.battery.get_range()


my_new_car = Car("audi", "a4", 2018, "black")
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

my_used_car = Car("subaru", "outback", 2015, "blue")
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.fill_gas_tank()

