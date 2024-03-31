import sys
from flask import Flask
import json
import argparse
import shortuuid
app = Flask(__name__)

gameDictionary = {'testid': 'X'}

# check to see if the given player has won the game
def check_win(boardState, piece):
    # check for all possible row wins
    for row in range(6):
        for startCol in range(4):
            linearIndex = row * 7 + startCol
            if boardState[linearIndex] == piece and boardState[linearIndex+1] == piece and boardState[linearIndex+2] == piece and boardState[linearIndex+3] == piece:
                return True
    # check for all possible col wins
    for col in range(7):
        for startRow in range(3):
            linearIndex = startRow * 7 + col
            if boardState[linearIndex] == piece and boardState[linearIndex+7] == piece and boardState[linearIndex+14] == piece and boardState[linearIndex+21] == piece:
                return True
    return False



# Given a column, drop a piece into that column and return the new board state
# Expects a 0-indexed column
def make_move(state, column, piece):
    boardState = state[2:]
    topRow = boardState[35:]

    # Check to make sure there's room in the column
    if topRow[column] != '-':
        return 'Error -- Chosen column is full'
    
    # Point to the top square in the column
    gravityPointer = 35 + column

    # "Drop" the pointer until a non-empty square is found
    while gravityPointer - 7 >= 0 and boardState[gravityPointer-7] == '-':
        gravityPointer -= 7
      
    # Now gravityPointer points to the bottom-most available square, so we add the new piece
    boardState = boardState[:gravityPointer] + piece[0] + boardState[gravityPointer + 1 :]

    print(boardState,    file=sys.stderr)
    
    return boardState

@app.route('/')
def hello_world():
    return 'Connect 4 API for Advanced Software Design'

@app.route('/newgame/<player>')
def new_game(player):
    if player != 'X' and player != 'O':
      return json.dumps('Error -- Player must be X or O')
    
    game_id = 'testid' # shortuuid.uuid()
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
    return make_move(state, 0, computerPlayer)


    
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Sample flask application')
    parser.add_argument('host')
    parser.add_argument('port', type=int)
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)