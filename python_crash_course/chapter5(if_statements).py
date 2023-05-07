'''
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

requested_toppings = ["mushrooms", "onions", "pineapple"]

banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
'''
'''
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
'''
'''
age = 47

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is {price}€.")
'''
'''
requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
'''
'''
# 5.3 exercise
alien_color = ["yellow", "red", "green"]
if "green" in alien_color:
    print("You just earned 5 points.")

# 5.4 exercise
alien_color = "yellow"
if "green" in alien_color:
    print("You just got 5 points.")
else:
    print("You just got 10 points.")

# 5.5 exercise
alien_color = "red"
if alien_color == "green":
    print("earned 5 points")
elif alien_color == "yellow":
    print("earned 10 points")
elif alien_color == "red":
    print("earned 15 points")

# 5.6 exercise
age = 300
if age < 2:
    print("baby")
elif 2 < age < 4:
    print("toddler")
elif 4 < age < 13:
    print("kid")
elif 13 < age < 20:
    print("teenager")
elif 20 < age < 65:
    print("adult")
elif 65 < age:
    print("elder")

# 5.7 exercise
favorite_fruits = ["peach", "kiwi", "apple"]
if "banana" in favorite_fruits:
    print("You really like bananas!")
if "kiwi" in favorite_fruits:
    print("You really like kiwi!")
if "peach" in favorite_fruits:
    print("You really like peaches!")
if "apple" in favorite_fruits:
    print("You really like apples!")
if "pear" in favorite_fruits:
    print("You really like pears!")
'''
'''
available_toppings = ["mushrooms", "olives", "green peppers", 
                        "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
'''

# 5.8 + 5.9 exercise
usernames = ["admin", "josh", "syndra", "camille", "steve"]
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")      
else:
    print("We need to find some users!")

#5.10 exercise
current_users = ["pete", "adam", "eve", "zack", "tom"]
new_users = ["pete", "adam", "josh", "paul", "charlie"]
for user in new_users:
    print(user)
    if user.lower in current_users:
        print("You need to enter a new username!")
    else:
        print("This username is available.")

# 5.11 esercise
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("\n1st")
    elif number == 2:
        print("\n2nd")
    elif number == 3:
        print("\n3rd")
    else:
        print(f"\n{number}th")


