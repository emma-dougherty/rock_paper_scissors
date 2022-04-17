from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game
import random

@app.route('/')
def home ():
    return render_template('index.html', title='Play!')

@app.route('/play')
def playc ():
    return render_template('playcomputer.html', title='Play Computer!')

@app.route('/test')
def test ():
    return render_template('test.html', title='Test')

### This works with index.html for two players, but with play against computer endpoint, it causes problems. Have not been able to work out why - has to do with ["name1"] ###

# @app.route('/<player1_choice>/<player2_choice>', methods=['POST'])
# def play(player1_choice, player2_choice):
#     player1_name = request.form["name1"]
#     player2_name = request.form["name2"]
#     player1_choice = request.form["choice1"]
#     player2_choice = request.form["choice2"]
#     player1 = Player(player1_name, player1_choice)
#     player2 = Player(player2_name, player2_choice)
#     result = Game.play_game(player1, player2)
#     return render_template('result.html', title='Result', player1=player1_name, player2=player2_name, player1_choice=player1_choice, player2_choice=player2_choice, result=result)

@app.route('/<player_choice>/<computer_choice>', methods=['POST'])
def play_computer(player_choice, computer_choice):
    player_name = request.form["name"]
    player2_name = "Computer"
    computer = Player("Computer", computer_choice)
    computer.choice = random.choice(computer_choice)
    player_choice = request.form["choice"]
    player1 = Player(player_name, player_choice)
    player2 = Player(player2_name, computer_choice)
    result = Game.play_computer(player1, player2)
    return render_template('result.html', title='Result', player1=player_name, player2="Computer", player1_choice=player_choice, player2_choice=computer_choice, result=result)


