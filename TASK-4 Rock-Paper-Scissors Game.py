import random
import tkinter as tk 
from tkinter import messagebox


def get_computer_choice():
    return random.choice(["r", "p", "s"])

def winner(comp, user):
    if comp == user :
        return "It's a Tie!\n"
    if(comp == "r" and user == "s"):
        return "You Lose!!\n"
    if(comp == "p" and user == "r"):
        return "You Lose!!\n"
    if(comp == "s" and user == "p"):
        return "You Lose!!\n"
    else:
        return "You Win!\n"

def play_game(user_choice):
    global user_score, computer_score

    computer_choice = get_computer_choice()
    choices = {"r" : "Rock", "p" : "Paper", "s" : "Scissors"}
    
    result = f"Computer Chose : {choices[computer_choice]}\n"
    result += winner(computer_choice, user_choice)

    if "Win" in result :
        user_score += 1
    elif "Lose" in result :
        computer_score += 1

    
    result_label.config(text=result)
    score_label.config(text=f"Score - You : {user_score} | Computer : {computer_score}")

def exit_game():
    messagebox.showinfo("Game Over", f"Final Score - You : {user_score}, Computer : {computer_score}\nThanks for playing!")
    root.quit()

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

window_width = 1080
window_height = 845
screen_width = root.winfo_screenwidth()
screen_heigth = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_heigth - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


title_label = tk.Label(root, text = "Rock-Paper-Scissors", font = ("Arial", 16, "bold"))
title_label.pack(pady = 10)


result_label = tk.Label(root, text = "Make your move!", font = ("Arial", 24))
result_label.pack(pady = 10)

score_label = tk.Label(root, text = f"Score - You : {user_score} | Computer : {computer_score}", font=("Arial", 20))
score_label.pack(pady = 5)


frame = tk.Frame(root)
frame.pack(pady=20)

rock_button = tk.Button(frame, text = "Rock", font = ("Arial", 12, "bold"), width = 10, command = lambda: play_game("r"))
rock_button.grid(row=0, column=0, padx = 10)

paper_button = tk.Button(frame, text = "Paper", font = ("Arial", 12, "bold"), width = 10, command = lambda: play_game("p"))
paper_button.grid(row=0, column=1, padx = 10)

scissors_button = tk.Button(frame, text = "Scissors", font = ("Arial", 12, "bold"), width = 10, command = lambda: play_game("s"))
scissors_button.grid(row=0, column=2, padx = 10)

exit_button = tk.Button(root, text = "Exit", font = ("Arial", 22), width = 22, command = exit_game)
exit_button.pack(pady=250)

root.mainloop()