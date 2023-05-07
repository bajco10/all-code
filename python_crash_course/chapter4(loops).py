'''
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
'''
'''
# 4.1 exercise
pizzas = ["pepperoni", "quattro formaggi", "hawai"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")
'''
'''
#4.2 exercise
animals = ["dog", "cat", "rat"]
for animal in animals:
    print(f"A {animal} would make a great pet.")

print("Any of these animals would make a great pet!")
'''
'''
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

digits = list(range(1, 1000000))
print(min(digits))
print(max(digits))
print(sum(digits))

squares2 = [value**2 for value in range(1, 11)]
print(squares2)
'''
'''
#4-x exercises
for number in range(1, 21):
    print(number)

numbers_of_a_milion = list(range(1, 1000001))
print(sum(numbers_of_a_milion))

for number in range(1, 21, 2):
    print(number)

for multiple in range (0, 31, 3):
    print(multiple)

cubes = [value**3 for value in range(1, 11)]
print(cubes)
'''
'''
players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)
'''
'''
# 4.10 - 4.12 exercises
my_foods = ["pizza", "falafel", "carrot cake", "apple", "rice"]
print(f"The first three items in the list are: {my_foods[:3]}")
print(f"Three items from the middle of th elist are: {my_foods[1:4]}")
print(f"The last three items in the list are: {my_foods[-3:]} ")

pizzas = ["pepperoni", "quattro formaggi", "hawai"]
friend_pizzas = list(pizzas[:])
friend_pizzas.append("ham")
print(pizzas)
print(friend_pizzas)
'''
'''
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
'''
'''
# 4.13 exercise
foods = ("pasta", "pizza", "nachos", "chicken", "steak")
foods = ("pasta", "pizza", "hot-dog", "beef", "steak")
for food in foods:
    print(food)
'''




