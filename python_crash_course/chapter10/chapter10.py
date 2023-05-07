'''
# the keyword with closes the file once access to it is no longer needed
filename = 'python_study/chapter10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# exercises 10.1, 10.2

filename_exercise = "python_study/chapter10/learning_python.txt"

with open(filename_exercise) as exercise_object:
    lines1 = exercise_object.readlines()
    print(exercise_object.read())
that_string = ""
for line1 in lines1:
    that_string += line1.rstrip()
    print(line1)

# print(that_string)
print(len(that_string))

# 10.2
message = "I really like dogs."
print(message.replace('dog', 'cat'))
'''
'''
filename = "programming.txt"
with open(filename, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    
with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

with open(filename) as test:
    print(test.read())
'''
# exercises 10.3 - 10.5
'''
# 10.3
guest_file = "guest.txt"
with open(guest_file, "w") as file_object:
    name = input("Please enter your username: ")
    file_object.write(name)

# 10.4
guestbook_file = "guest_book.txt"
with open(guestbook_file, "w") as file_object:
    while True:
        name = input("Enter your username: ")
        if name == "q":
            break
        file_object.write(name+"\n")

# 10.5
programming_poll = "programming_poll.txt"

with open(programming_poll, "w") as file_object:
    while True:
        reason = input("Why do you like programming?\n")
        if reason == "q":
            break
        file_object.write(reason+"\n")
'''
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
         break
    
    try:
        answer = float(first_number)/float(second_number)
    except ZeroDivisionError:
        print("You can't divid by zero!")
    except ValueError:
        print("Please enter numbers, not letters!")
    else:
        print(answer)
'''
'''
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
           contents = f.read()
    except FileNotFoundError:
       print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = "alice.txt"
count_words(filename)

filenames = ["python_study/chapter10/alice.txt", "python_study/chapter10/siddhartha.txt", 
             "python_study/chapter10/moby_dick.txt", "python_study/chapter10/little_women.txt"]
for filename in filenames:
    count_words(filename)
'''
# exercises 10.6 - 10.10
'''
# 10.6, 10.7
while True:
    try:
        x = input("Enter the first number:")
        if x == "q":
            break
        x = float(x)
        y = input("Enter the second number:")
        if y == "q":
            break
        y = float(y)
        calculation = x+y
        print("Here is your result: "+ str(calculation))
    except ValueError:
            print("Enter numbers, not other stuff!")

try:
    with open("python_study/chapter10/cats.txt", "r") as cats:
        cat_names = cats.read()
        print("Cat names:\n", cat_names)
    with open("python_study/chapter10/dogs.txt", "r") as dogs:
        dog_names = dogs.read()
        print("Dog names:\n", dog_names)
except FileNotFoundError:
    pass


with open("python_study/chapter10/beyond_good_and_evil.txt") as book:
    ready = book.read()
    counting = ready.lower().count("the")
    print(ready)
    print(counting)
'''

from fileinput import filename
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = "numbers.json"
with open(filename, "w") as f:
    json.dump(numbers, f)

filename = "numbers.json"
with open(filename) as f:
    numbers = json.load(f)
print(numbers)









