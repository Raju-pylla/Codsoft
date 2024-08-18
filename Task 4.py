import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    choices = ['Rock', 'Paper', 'scissor']
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    if (user_choice == 'Rock' and computer_choice == ['scissor']) or \
       (user_choice == 'Paper' and computer_choice in ['Rock']) or \
       (user_choice == 'scissor' and computer_choice in ['Paper']):
        return 'You win!'
    return 'Computer wins!'

# Function to handle the user's choice
def user_choice(choice):
    computer_choice = random.choice(['Rock', 'Paper', 'scissor'])
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    play_again_button.pack()

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, scissor")

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: user_choice('Rock'))
paper_button = tk.Button(root, text="Paper", command=lambda: user_choice('Paper'))
caesar_button = tk.Button(root, text="scissor", command=lambda: user_choice('scissor'))

# Create a label to show the result
result_label = tk.Label(root, text="Choose Rock, Paper, or scissor")

# Create a button to play again
def play_again():
    result_label.config(text="Choose Rock, Paper, or scissor")
    play_again_button.pack_forget()

play_again_button = tk.Button(root, text="Play Again", command=play_again)

# Arrange the widgets in the window
rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
caesar_button.pack(side=tk.LEFT, padx=10)
result_label.pack(pady=20)

# Start the main loop
root.mainloop()