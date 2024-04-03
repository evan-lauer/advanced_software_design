import sys
import shortuuid
from flask import Flask
import json
import argparse
import random

app = Flask(__name__)

games = {}

@app.route('/newgame/<player>')
def newGame(player):
    game_id = shortuuid.uuid()
    games[game_id] = player
    return json.dumps({'ID':game_id})



#assuming that we are starting at the bottom
@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def nextMove(gameID, oppCol, state):
    if gameID in games:
        player = state[0]
        win = player * 3
        state = state[2:]

        if player == games[gameID]:

            #check for winnning moves
            check_rows(state, win)
            check_columns(state, win)
            check_diagonals(state, win)

            #if no winning move, play a radnom column
            done = false
            while not done:
                index = random.randint(-6, -1):
                if state[index] == "-":
                    #put the piece in this column
                    done = True
    
        


         
#a method to check for a winning opportunity in the rows
def check_rows(state, win):
    i = 0
    while i < 42:
        row = state[i:i+7]
        #if there is an opportunity to win, take it
        if (('-'+ win) in row): 
            index = row.index('-'+ win)
            index = i + index
            #placing the element at the correct index
            tempList = [*state]
            tempList[index] = player
            return json.dumps(''.join(map(str, tempList)))
        elif ((win +'-') in row):
            index = row.index(win +'-')
            index = i + index + 3 #different form the prior case
            #placing the element at the correct index
            tempList = [*state]
            tempList[index] = player
            return json.dumps(''.join(map(str,tempList)))

        i += 7




#a method to check for a winning opportunity in the columns
def check_columns(state, win):
    for i in range(7):
        bottom = i
        column = [state[i]]
        for j in range(5):
            bottom += 7
            column.append(state[bottom])
        column = ''.join(map(str, column))
        #if there is an opportunity to win, take it
        if (win + '-') in column:
            index = column.index(win +'-') + 3
            index = i + (7 * index)
            #placing the element at the correct index
            tempList = [*state]
            tempList[index] = player
            return json.dumps(''.join(map(str,tempList)))

#a method to check for a winning opportunity in the diagonals
def check_diagonals(state, win):
    for i in [14, 7, 0, 1, 2, 3]:
        bottom = i
        diagonal = []
        while bottom < 42:
            diagonal.append(state[bottom])
            bottom += 8
        diagonal = ''.join(map(str, diagonal))
        #if there is an opportunity to win, take it
        if (win + '-') in diagonal:
            index = diagonal.index(win +'-') + 3
            index = i + (8 * index)
            #placing the element at the correct index
            tempList = [*state]
            tempList[index] = player
            return json.dumps(''.join(map(str,tempList)))



            


            

        #return json.dumps(rows)

        # for i in state:
        #     if i == 'X':
        #         xCount+=1
        #     elif i == 'O':
        #         oCount+=1
        #     elif i != '-':
        #         return json.dumps('Error: invalid board state')
        
        
        # if player == 'X':
        #     diff = xCount - oCount
        # elif player == 'O':
        #     diff = oCount - xCount
        # else:
        #     return json.dumps('Error: invalid player')
    

    else:
        return json.dumps('Error: game does not exist')
    return json.dumps(0)


@app.route('/games')
def seeGames():
    return json.dumps(games)

if __name__ == '__main__':
    host = 'localhost'
    port = 5555
    app.run(host=host, port=port, debug=True)
