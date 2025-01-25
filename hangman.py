import string
import os
import random
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class HangmanGame:
    def __init__(self):
        self.word_list = [
            'stun', 'amuse', 'comment', 'systematic', 'adviser', 'argument', 
            'chemistry', 'ward', 'goal', 'knot', 'confession', 'desk', 
            'opinion', 'dilute', 'horoscope', 'number', 'overall', 'dark', 
            'girl', 'association', 'reserve', 'shrink', 'autonomy', 'worker', 
            'confrontation', 'mountain', 'conception', 'corpse', 'prestige', 
            'family', 'belief', 'mobile', 'trouble', 'temptation'
        ]
        self.reset_game()

    def reset_game(self):
        self.played_word = random.choice(self.word_list)
        self.gameboard = ['_'] * len(self.played_word)
        self.gameboard_finished = list(self.played_word)
        self.guess_archive = ['Guesses:']
        self.lives = ['Chances(7):']
        self.end_state = False

    def make_guess(self, player_guess):
        player_guess = player_guess.lower()
        
        if player_guess in self.guess_archive:
            return "Already guessed"
        
        self.guess_archive.append(player_guess)
        
        if player_guess in self.played_word:
            for pos, char in enumerate(self.played_word):
                if char == player_guess:
                    self.gameboard[pos] = player_guess
            return "Correct"
        else:
            self.lives.append('x')
            return "Incorrect"

    def check_game_status(self):
        if len(self.lives) == 8:
            return "Lost"
        if self.gameboard == self.gameboard_finished:
            return "Won"
        return "Continue"

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.game = HangmanGame()
        
        master.title("Hangman Game")
        master.geometry("605x390")
        master.resizable(0, 0)
        master.configure(background="RosyBrown3")
        
        self.setup_ui()
        self.create_letter_buttons()

    def setup_ui(self):
        self.gui_gameboard = tk.Label(
            self.master, 
            text=' '.join(self.game.gameboard), 
            font="Verdana 30 bold", 
            bg="RosyBrown3"
        )
        self.gui_gameboard.pack(side="top")

        self.gui_guess_archive = tk.Label(
            self.master, 
            text=', '.join(self.game.guess_archive), 
            font="Verdana 12 bold", 
            bg="RosyBrown3", 
            fg='purple'
        )
        self.gui_guess_archive.pack()
        self.gui_guess_archive.place(bordermode=tk.OUTSIDE, x=200, y=260)

        self.gui_lives = tk.Label(
            self.master, 
            text=' '.join(self.game.lives), 
            font="Verdana 12 bold", 
            fg='purple', 
            bg="RosyBrown3"
        )
        self.gui_lives.pack()
        self.gui_lives.place(bordermode=tk.OUTSIDE, x=200, y=280)

        # Load hangman image
        try:
            image = Image.open('download.png')
            self.image = ImageTk.PhotoImage(image)
            image_label = tk.Label(
                self.master, 
                image=self.image, 
                width=300, 
                height=300, 
                bg="RosyBrown3"
            )
            image_label.pack()
            image_label.place(bordermode=tk.OUTSIDE, x=410, y=160)
        except FileNotFoundError:
            print("Hangman image not found")

    def create_letter_buttons(self):
        letters = list(string.ascii_lowercase)
        positions = [
            (60, 0), (60, 50), (60, 100), (60, 150), (60, 200)
        ]
        
        for i, letter in enumerate(letters):
            row = i // 6
            col = i % 6
            
            btn = tk.Button(
                self.master, 
                text=letter.upper(), 
                command=lambda l=letter: self.on_letter_click(l),
                bg="RosyBrown3",
                height=2,
                width=5
            )
            btn.place(x=positions[row][0] + col*100, y=positions[row][1])

    def on_letter_click(self, letter):
        result = self.game.make_guess(letter)
        
        # Update UI elements
        self.gui_gameboard['text'] = ' '.join(self.game.gameboard)
        self.gui_guess_archive['text'] = ', '.join(self.game.guess_archive)
        self.gui_lives['text'] = ' '.join(self.game.lives)
        
        # Check game status
        status = self.game.check_game_status()
        if status == "Won":
            messagebox.showinfo("Congratulations!", "You won!")
            self.master.quit()
        elif status == "Lost":
            messagebox.showinfo("Game Over", f"You lost! The word was: {self.game.played_word}")
            self.master.quit()

def main():
    root = tk.Tk()
    game_gui = HangmanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()