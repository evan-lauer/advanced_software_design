#! /usr/bin/python
# A simple API endpoint to be used for a game of connect4
# Mary Blanchard, Warren Kozak, Noah Lee

import flask
import random

app = flask.Flask(__name__)

# Store a list of existing games
existing_games = {}


def replacer(s, index, newstring):
    return s[:index] + newstring + s[index+1:]

# New game


@app.route('/newgame/<player>')
def newGame(player):
    waiting = True
    while waiting:
        newID = random.randint(1000, 2000)
        if newID not in existing_games:
            existing_games[newID] = player
            return flask.jsonify({
                'ID': newID
            })

# Existing game


@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def nextMove(gameID, oppCol, state):
    board = state
    id = gameID
    oC = int(oppCol)
    columns = []

    for i in range(7):  # 7 columns
        column = ''
        for j in range(6):  # 6 rows
            index = j * 7 + i
            column += board[index]
        columns.append(column)

    # if oppCol is 3, nums would be
    topBox = (6*6)+oC-1
    for i in range(topBox, 0, -7):
        boardBox = board[i]
        if boardBox != '-':
            if boardBox == 'X':
                player = 'O'  # if the last player's move was an X, set the current move as an O
            else:
                player = 'X'  # if the last player's move was an O, set the current move as an X

    success = False
    numTries = 0
    while not success or numTries > 30:  # 30 is an arbitrary amount of tries
        randCol = random.randint(0, 6)
        column = columns[randCol]
        # Find the first empty slot from the bottom of the column
        emptySlot = column.find('-')
        if emptySlot != -1:  # find returns -1 if it doesnt find anything
            # Calculate the index in the string
            index = emptySlot * 7 + randCol
            board = replacer(board, index, player)
            success = True
        else:
            # If the selected column is full, try another one
            numTries += 1
            continue

    return flask.jsonify({'ID': id, 'Col': column, 'State': board})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5127, debug=True)
