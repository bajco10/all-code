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
    lbl_result.config(text=f"Player: {player_choice}\nComputer: {computer_choice}\n\n{result}")
window = tk.Tk()
window.title("Rocks, Paper, Scissors")
#window.rowconfigure(0, weight=1)
#window.rowconfigure(1, minsize=150, weight=1)

# result label
lbl_result = tk.Label(window, text="Choose an option to play!", width=27, height=10)
# player option frame
frm_options = tk.Frame(window, relief=tk.RAISED, borderwidth=2)
# player option buttons
btn_rock = tk.Button(master=frm_options, text="Rock", width=9, height=2, command=lambda: play_game("Rock"))#, sticky="nsew")
btn_paper = tk.Button(master=frm_options, text="Paper", width=9, command=lambda: play_game("Paper"))#, sticky="nsew")
btn_scissors = tk.Button(master=frm_options, text="Scissors", width=9, command=lambda: play_game("Scissors"))#, sticky="nsew")
# placing option buttons into option frame
btn_rock.grid(row=0, column=0, sticky="nsew")
btn_paper.grid(row=0, column=1, sticky="nsew")
btn_scissors.grid(row=0, column=2, sticky="nsew")
# placing the whole GUI together
lbl_result.grid(row=0, column=0, sticky="nsew")
frm_options.grid(row=1, column=0)

window.mainloop()


