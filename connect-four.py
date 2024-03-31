import sys
from flask import Flask
import json
import argparse
import shortuuid
app = Flask(__name__)

gameDictionary = {}

def check_win():
    # check to see if the given player has won the game





def make_move(state, column):
    # given a column, drop a piece into that column and return the new board state
    boardState = state[2:]
    topRow = boardState[35:]
    return json.dumps()

@app.route('/')
def hello_world():
    return 'Connect 4 API for Advanced Software Design'

@app.route('/newgame/<player>')
def new_game(player):
    if player != 'X' and player != 'O':
      return json.dumps('Error -- Player must be X or O')
    
    game_id = shortuuid.uuid()
    if player == 'X':
        gameDictionary[game_id] = 'X'
    else:
        gameDictionary[game_id] = 'O'
    return json.dumps({'ID': game_id})

@app.route('/seegames')
def show_games():
    return json.dumps(gameDictionary)

@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def next_move(gameID, oppCol, state):
    
    computerPlayer = gameDictionary[gameID]

    if computerPlayer != state[0]:
        return json.dumps("Error -- It's the player's turn")


    
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Sample flask application')
    parser.add_argument('host')
    parser.add_argument('port', type=int)
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)