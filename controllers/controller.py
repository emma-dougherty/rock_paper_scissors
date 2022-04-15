from flask import render_template
from app import app
from models.player import Player
from models.game import Game

@app.route('/')
def home ():
    return render_template('index.html', title='Play!')

@app.route('/<player1_choice>/<player2_choice>')
def play(player1_choice, player2_choice):
    player1 = Player("Player 1", player1_choice)
    player2 = Player("Player 2", player2_choice)
    result = Game.play_game(player1, player2)
    return render_template('result.html', title='Result', result=result)
