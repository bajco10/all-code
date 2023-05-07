import json
from fileinput import filename

def get_favorite_number():
    filename = "favorite_number.json"
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    number = input("What is your favorite number? ")
    filename = "favorite_number.json"
    with open(filename, "w") as f:
        json.dump(number, f)
    return number

def print_number():
    number = get_favorite_number()
    if number:
        print(f"You favorite number is: {number}")
    else:
        number = get_new_number()
        print(f"Now I know that your fav number is: {number}")

print_number()







