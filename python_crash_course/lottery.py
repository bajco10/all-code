from math import factorial
from random import choice, choices
lottery_list = [4, "j", "k", "o", "w", "q", 3, 5, 23, 111, 423, 22, 122, 1, 12]


print("Those things are winning: ")
winning_choices = choices(lottery_list, k=4)


my_ticket = ["j", 111, 22, 122, 1, 12]
number_of_pulls = 0

while my_ticket != winning_choices:
    winning_choices = choices(lottery_list, k=6)
    number_of_pulls = number_of_pulls + 1
    if my_ticket == winning_choices:
        print(f"the number of pulls is: {number_of_pulls}")
        break

print()
print(factorial(10))


    
    


