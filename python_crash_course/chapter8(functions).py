'''
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}!")

greet_user("jack")
greet_user("sarah")
greet_user("noel")
'''
# exercises 8.1 - 8.2
'''
def display_message():
    print("I am learning about functions in this chapter!")

display_message()


def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.")

favorite_book("Beyond good and evil")
'''
'''
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("harry", "hamster")
describe_pet("rat", "ringla")

pets = {
    "hamster": "harry",
    "rat": "ringla",
    "dog": "zoro",
}

for type, name in pets.items():
    describe_pet(type, name)
# using KEYWORD ARGUMENTS
describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")

describe_pet(pet_name="sjuzn")
describe_pet("willie")
describe_pet(pet_name="alica", animal_type="cat")
'''
# exercises 8.3 - 8.5
'''
# 8.3
def make_shirt(size, text_on_shirt):
    print(f"The size of the shirt is {size.upper()} with {text_on_shirt} being printed on it. ")

make_shirt("xxl", "yeah boi")

# 8.5
def describe_city(city, country = "slovakia"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("martin", "slovakia")
describe_city("bratislava")
describe_city("reykjavik", "iceland")
'''
'''
def get_formatted_name(first_name, last_name, middle_name = ""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
    

musician = get_formatted_name("jimi", "hendrix")
print(musician)

musician2 = get_formatted_name("john", "lee", "hooker")
print(musician2)


def build_person(first_name, last_name, age=None):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician3 = build_person("jimi", "hendrix", 47)
print(musician3)
'''
'''
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
'''
# exercises 8.6 - 8.8
"""
# 8.6
def city_country(city, country):
    print(f"{city.title()}, {country.title()}")

city_country("martin", "slovakia")
city_country("bratislava", "slovakia")
city_country("berlin", "germany")

# 8.7, 8.8
def make_album(artist_name, album_title):
    album = {"name": artist_name, "title": album_title}
    return album
while True:
    print("\nEnter the name of the artist:")
    print("\n press 'q' to quit")

    artist_name = input("Artists name: ")
    if artist_name == "q":
        break
    
    album_title = input("Album title: ")
    if album_title == "q":
        break

    album_info = make_album(artist_name, album_title)
    print(album_info)
"""
'''
def greet_users(names):
    """Print a simple greetin to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ["hannah", "ty", "margot", "john", "shawn"]
greet_users(usernames)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
'''
# exercises 8.9 - 8.11
'''
# 8.9 & 8.10
def send_messages(short_messages, sent_messages):
    while short_messages:
        current_message = short_messages.pop()
        print(f"Seding: {current_message.title()}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent: ")
    for sent_message in sent_messages:
        print(sent_message)

short_messages = ["I am busy at the moment.", "Please call later.", "Call me maybe."]
sent_messages = []
send_messages(short_messages, sent_messages)
show_sent_messages(sent_messages)
'''
'''
def make_pizza(size, *toppings):
    print(f"\nMakinga a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "gree peppers", "extra cheese")
'''
'''
from statistics import mode


def build_prifle(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_prifle("albert", "einstein", location="princeton", field="physics")
print(user_profile)
'''
# exercises 8.12 - 8.14
'''
# 8.12
def sandwich_function(*items):
    print(f"A {items} sandwich is being ordered. ")

sandwich_function("butter", "olives", "milk")
sandwich_function("coal")
sandwich_function("toast", "beans")

# 8.14

def car_information(manufacturer, model, **othr):
    information = manufacturer, model, othr
    print(information)

car = car_information("subaru", "outback", color="blue", tow_package=True)
'''
# exercises 8.15-8.17





