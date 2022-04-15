from models.player import *

class Game():

    def play_game(player1, player2):
        if player1.choice == "rock" and player2.choice == "scissors":
            return " Player1 wins by playing " + player1.choice
        
        if player1.choice == "scissors" and player2.choice == "paper":
            return " Player1 wins by playing " + player1.choice
        
        if player1.choice == "paper" and player2.choice == "rock":
            return " Player1 wins by playing " + player1.choice
        
        if player1.choice == player2.choice:
            return None

        return " Player2 wins by playing " + player2.choice







