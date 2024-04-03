# Helper functions for connect 4 logic and board formatting
# Mary Blanchard, Warren Kozak, Noah Lee

def validboard(board:str):
    '''Validates that a board string is valid.'''
    #Currently this just checks length but we could look for 
    #non-allowed characters or invalid piece configurations if we want to be fancy.
    if len(board) != 42:
        return False
    return True

def printboard(board:str):
    '''Prints out a board. If board string is not of correct length, return 0. Otherwise return 1.'''
    if not validboard(board):
        return False
    print(board[35:])
    print(board[28:35])
    print(board[21:28])
    print(board[14:21])
    print(board[7:14])
    print(board[0:7])
    return True

def placepiece(board:str, player:str, location:int):
    '''Inserts the player string at the location specified on the board.'''
    if location > 41 or not validboard(board):
        print("error placing piece. returning old board.")
        return board
    newboard = board[0:location] + player + board[location+1:]
    return newboard