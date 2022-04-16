from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game

@app.route('/')
def home ():
    return render_template('index.html', title='Play!')

@app.route('/<player1_choice>/<player2_choice>', methods=['POST'])
def play(player1_choice, player2_choice):
    player1_name = request.form["name1"]
    player2_name = request.form["name2"]
    player1_choice = request.form["choice1"]
    player2_choice = request.form["choice2"]
    player1 = Player(player1_name, player1_choice)
    player2 = Player(player2_name, player2_choice)
    result = Game.play_game(player1, player2)
    return render_template('result.html', title='Result', player1=player1_name, player2=player2_name, player1_choice=player1_choice, player2_choice=player2_choice, result=result)

