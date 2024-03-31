import sys
import shortuuid
from flask import Flask
import json
import argparse
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
    if True: #gameID in games:

        # xCount = 0
        # oCount = 0
        player = state[0]
        win = player * 3
        state = state[2:]
        temp_state = state
        rows = []
    
        #for i in range(6):
            # str = temp_state[:7]
            # rows.append(str)
            # print(str)
            # temp_state = temp_state[8:]
        

        #rows
        # i = 0
        # while i < 42:
        #     row = state[i:i+7]
        #     if (('-'+ win) in row): 
        #         index = row.index('-'+ win)
        #         index = i + index
        #         tempList = [*state]
        #         tempList[index] = player
        #         return json.dumps(''.join(map(str, tempList)))
        #     elif ((win +'-') in row):
        #         index = row.index(win +'-')
        #         index = i + index + 3 #different form the prior case
        #         tempList = [*state]
        #         tempList[index] = player
        #         return json.dumps(''.join(map(str,tempList)))

        #     i += 7
        


        #columns
        for i in range(7):
            column = [state[i]]
            for j in range(5):
                column.append(state[i+7])
            if (win + '-') in column:
                index = column.index(win +'-') + 3
                index = i + (7 * index)
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
