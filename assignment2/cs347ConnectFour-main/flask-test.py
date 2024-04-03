# Mary Blanchard, Warren Kozak, Noah Lee

import flask
import json
import random

app = flask.Flask(__name__)

# New game
theDict = {}  # id  : player


def replacer(s, index, newstring):
    return s[:index] + newstring + s[index+1:]


@app.route('/newgame/<player>')
def newGame(player):
    global theDict
    theDict[2387] = player
    the_dictionary = {'ID': '2387'}  # ID: num
    return flask.jsonify(the_dictionary)


# Next Move
@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def nextMove(gameID, oppCol, state):

    # Read in state
    gameID = int(gameID)
    oppCol = int(oppCol)
    player = state.split('#')[0]
    board = state.split('#')[1]

    columns = []

    for i in range(7):  # There are 7 columns in Connect Four
        column = ''
        for j in range(6):  # There are 6 rows in Connect Four
            index = j * 7 + i
            column += board[index]
        columns.append(column)

    success = False
    numTries = 0

    while not success or numTries > 30:
        randCol = random.randint(0, 6)  # Select a random column
        column = columns[randCol]
        # Find the first empty slot from the bottom of the column
        emptySlot = column.find('-')
        if emptySlot != -1:
            # Calculate the index in the string
            index = emptySlot * 7 + randCol
            board = replacer(board, index, player)
            success = True
        else:
            # If the selected column is full, try another one
            numTries += 1
            continue

    # Return new board state
    return flask.jsonify({'ID': gameID, 'Col': randCol, 'State': board})


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5127
    app.run(host=host, port=port, debug=True)
