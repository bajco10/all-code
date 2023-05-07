'''
alien_0 = {"color" : "green", "points" : 5}
print(alien_0["color"])
print(alien_0["points"])
new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

print(alien_0)
alien_0["x_position"] = 0
alien_0["y_positions"] = 25
print(alien_0)
'''
'''
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)

print(f"The alien is {alien_0['color']}")
alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")
'''
'''
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")

alien_0["speed"] = "fast"

# move the alien to the right.
# determine how far to move the alien based on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # fast af alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"New position: {alien_0['x_position']}")
'''
'''
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)
'''
'''
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")
'''
'''
alien_0 = {"color": "green", "speed": "slow"}

point_value = alien_0.get("points", "No point value assigned.")
print(point_value)
'''
'''
# 6.1 
familiar_person = {"first_name": "Martin",
                    "last_name": "Medek",
                    "age": 18,
                    "city": "Martin",
                    }

print(familiar_person)

# 6.2
favorite_numbers = {"tom": 10,
                    "mark": 1,
                    "jane": 9,
                    "pete":69,
                    "josh": 7,}
print(favorite_numbers)

# 6.3
programming_words = {"run": "to start a program",
                    "debug": "go through the program to find bugs",
                    "string": "a variable to store text in",
                    "integer": "a variable to store whole number in",
                    "boolean": "a variable for True/False state",
                    }
print(f"\nRun - {programming_words['run']}")
print(f"\nDebug - {programming_words['debug']}")
print(f"\nString - {programming_words['string']}")
print(f"\nInteger - {programming_words['integer']}")
print(f"\nBoolean - {programming_words['boolean']}")
'''
'''
user_0 = {
    "username": "efermi",
    "first_name": "enrico",
    "last_name": "fermi",
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")
'''
'''
favorite_languages = {
                    'jen': 'python',
                    'sarah': 'c',
                    'edward': 'ruby',
                    'phil': 'python',
                    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())
'''
'''
# 6.4
programming_words = {"run": "to start a program",
                    "debug": "go through the program to find bugs",
                    "string": "a variable to store text in",
                    "integer": "a variable to store whole number in",
                    "boolean": "a variable for True/False state",
                    "loop": "used for repeating a line of code",
                    "print": "a function to display data to the user",
                    "code": "text for computer to execute",
                    "key-value pair": "a dictionary consists of those",
                    }

for word, meaning in programming_words.items():
    print(f"{word.title()} - {meaning.title()}")

# 6.5
countries_and_rivers = {"Egypt": "Nile",
                        "Congo": "Congo river",
                        "Brazil": "Amazon"}

for country, river in countries_and_rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
                  
for river in countries_and_rivers.values():
    print(river.title())

for country in countries_and_rivers.keys():
    print(country.title())

# 6.6
'''
'''
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Change the first 3 aliens
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Toatal number of aliens: {len(aliens)}")
'''
'''
# Store information about a pizza bein ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
        }
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
        "with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t{topping}")
'''
'''
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t {language.title()}")
'''
# important note
'''
You should not nest lists and dictionaries too deeply. If you're 
nesting items much deeper than wat you see in the preceding examples or 
you're working with someone else's code with significant levels of nesting, 
most likely a simpler way to selve the problem exists.
'''
'''

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    '''
# exercises
'''
# 6.8
pets = []
pet_0 = {
    "specie": "rat",
    "owner": "tom",
}

pet_1 = {
    "specie": "horse",
    "owner": "vera",
}

pet_2 = {
    "specie": "dog",
    "owner": "majo",
}

pets.append(pet_0)
pets.append(pet_1)
pets.append(pet_2)

for pet in pets:
    print(pet["specie"].title() + " is " + pet["owner"].title() + "'s pet!")

# 6.9
favorite_places = {
    "tom": "norway",
    "joe": "alabama",
    "richard": "texas",
}

for name, place in favorite_places.items():
    print(f"{place.title()} is {name.title()}'s favorite place.")

# 6.11
cities = {
    "bratislava": {
        "country": "slovakia",
        "population": "424 428",
        "fact": "The city sits on two majestic rivers.",
    },
    "tokyo": {
        "country": "japan",
        "population": "13 960 000",
        "fact": "Was called Edo for a very long time."
    },
    "oslo": {
        "country": "norway",
        "population": "634 293",
        "fact": "Most of Oslo consists of forest.",
    },
}

for city, information in cities.items():
    print(f"{city.title()}: ")
    country = information["country"]
    population = information["population"]
    fact = information["fact"]
    print(f"\t{country.title()}")
    print(f"\t{population}")
    print(f"\t{fact}")
'''









