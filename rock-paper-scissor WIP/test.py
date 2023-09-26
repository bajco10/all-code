import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play_game(player_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    show_result(player_choice, computer_choice, result)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "Player wins"
    else:
        return "Computer wins"

def show_result(player_choice, computer_choice, result):
    result_label.config(text=f"Player chose: {player_choice}\nComputer chose: {computer_choice}\nResult: {result}\n \n \n \n \n \n")

root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Player Buttons
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game("Rock"))
rock_button.pack(side="left", padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game("Paper"))
paper_button.pack(side="left", padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game("Scissors"))
scissors_button.pack(side="left", padx=10, pady=10)

# Result Label
result_label = tk.Label(root, text="Choose an option to play!")
result_label.pack(pady=20)

root.mainloop()

