from models.player import *

from random import *
class Game():

    def play_game(player1, player2):
        if player1.choice == "rock" and player2.choice == "scissors":
            return " Player 1 wins by playing " + player1.choice
        
        if player1.choice == "scissors" and player2.choice == "paper":
            return " Player 1 wins by playing " + player1.choice
        
        if player1.choice == "paper" and player2.choice == "rock":
            return " Player 1 wins by playing " + player1.choice
        
        if player1.choice == player2.choice:
            return None

        return " Player 2 wins by playing " + player2.choice

    def play_computer(human):
        computer = "Computer"
        computer.choice = random.choice("rock","paper","scissors")

        if human.choice == "rock" and computer.choice == "scissors":
            return " Player 1 wins by playing " + human.choice
        
        if human.choice == "scissors" and computer.choice == "paper":
            return " Player 1 wins by playing " + human.choice
        
        if human.choice == "paper" and computer.choice == "rock":
            return " Player 1 wins by playing " + human.choice
        
        if human.choice == computer.choice:
            return None

        return "Computer wins by playing " + computer.choice








