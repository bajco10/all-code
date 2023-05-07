from optparse import IndentedHelpFormatter
from secrets import choice
from chapter9 import Restaurant
from chapter9 import User
from chapter9 import Admin
from chapter9 import Privilidges

my_restaurant = Restaurant("pizza pub korea", "whatever we have")
my_restaurant.describe_restaurant()
my_restaurant.increment_number_served(2090)
my_restaurant.describe_restaurant()

user1 = User("tom", "bajo", 18, "sucany", "student")
user1.describe_user()

user2 = Admin("majo", "vajo", 82, "martin", "artist")
user2.describe_user()
user2 = Privilidges()
user2.show_priviliges()

from random import randint
print(randint(1,6))

from random import choice
players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print(first_up)

# 275
