import random
def game():
    print("Let's play Rock, Paper, Scissors!")
    print("Choose one: (1) Rock, (2) Paper, (3) Scissors")
    
    choices = ["Rock", "Paper", "Scissors"]
    
    while True:
        player_choice = int(input("Enter your choice (1-3): "))
        
        if player_choice in [1, 2, 3]:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
    
    player_choice -= 1
    computer_choice = random.randint(0, 2)
    print("You chose:", choices[player_choice])
    print("Computer chose:", choices[computer_choice])
    result = (player_choice - computer_choice) % 3
    print(result)
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("You win!")
    else:
        print("Computer wins!")

game()

    