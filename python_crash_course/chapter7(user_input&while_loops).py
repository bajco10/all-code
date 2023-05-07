'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Plase enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your first name? "
name = input(prompt)

print(f"\nHello, {name}!")
'''
'''
age = input("How old are you?!\n")
age = int(age)
if age >= 18:
    print("True")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
'''
# exercises 7.1 - 7.3
'''
# 7.1
car = input("What kind of a rental car would you like?\n")
print(f"\nLet me find you a {car}.")

# 7.2
number_of_people = input("How many people are in your dinner group?\n")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

# 7.3
number = input("Give me a number and I'll tell you if it's a multiple of 10.\n")
number = int(number)
if number % 10 == 0:
    print("Your numer is a multiple of 10!")
else:
    print("Your number is not a multiple of 10.")
'''
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
'''
# "parrot program" but with use of the so called "FLAG"
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print("The program has quit.")
    else:
        print(message)
'''
'''
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)\n"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"Ipd love to go to {city.title()}!")
'''
'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
'''
# exercises 7.4 - 7.6
'''
# 7.4
prompt = "\nPlease enter series of pizza toppings."
prompt += "\nEnter 'quit' to end.\n"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"Adding {toppings} to your pizza!\n")
# 7.5
prompt = ("Enter your age to get the price of your ticket: \n")

while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
        break
    elif 3 < age < 12:
        print("The price of your ticket is 10€.")
        break
    else:
        print("The price of your ticket is 15€. ")
        break
'''
'''
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''
'''
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)

while "dog" in pets:
    pets.remove("dog")

print(pets)
'''
'''
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let aonther person respond? (y/n) ")
    
    if repeat == "n":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
'''
# exercises 7.8 - 7.10
'''
# 7.8 & 7.9
sandwich_orders = ["chicken","pastrami", "egg","pastrami", "seafood", "roast beef", "ham", "pastrami"]
finished_sandwiches = []
print("Sorry, the deli ra out of pastrami :(.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    currently_in_making = sandwich_orders.pop()
    print(f"I made your {currently_in_making} sandwich! ")
    finished_sandwiches.append(currently_in_making)

for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich was made. ")
# 7.10

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    destination = input("\nWhich destination is your dream vacation? ")

    responses[name] = destination

    repeat = input("Would you like to let another person respend? (y/n)\n")

    if repeat == "n":
        polling_active = False

print("\n--- Pol Results ---")
for name, destination in responses.items():
    print(f"{name.title()}'s dream vacation destination is {destination.title()}. ")
'''
