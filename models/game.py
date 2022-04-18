import random
from models.player import *

class Game():

    def play_game(player1, player2):
        if player1.choice == "rock" and player2.choice == "scissors":
            return f"Player 1 wins by playing {player1.player_choice}"
        
        if player1.choice == "scissors" and player2.choice == "paper":
            return f"Player 1 wins by playing {player1.choice}"
        
        if player1.choice == "paper" and player2.choice == "rock":
            return f"Player 1 wins by playing {player1.choice}"
        
        if player1.choice == player2.choice:
            return None

        return " Player 2 wins by playing " + player2.choice

    def play_computer(human, computer):
        computer_choice = ["rock","paper","scissors"]
        computer = Player("Computer", computer_choice)
        computer.choice = random.choice(computer_choice)

        if human.choice == "rock" and computer.choice == "scissors":
            return f"Player 1 wins by playing {human.choice}"
        
        if human.choice == "scissors" and computer.choice == "paper":
            return f"Player 1 wins by playing {human.choice}"
        
        if human.choice == "paper" and computer.choice == "rock":
            return f"Player 1 wins by playing {human.choice}"
        
        if human.choice == computer.choice:
            return None

        return f"Computer wins by playing {computer.choice}"







