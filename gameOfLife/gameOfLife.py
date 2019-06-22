import random
import copy
import pdb

log = open("errorLog","w+")

height = 10
width = 10
alive = 1
dead = 0

# a tuple of tuples with dim width x height
deadState = [[dead]*width for _ in range(height)]

#pdb.set_trace();
# randomize the boardState
randomState = copy.deepcopy(deadState)

for i in range(height):
    for j in range(width):
        randomState[i][j] = random.randint(0,1)

def  printBoard(board):
    # print board state like a board
    rowStr = ""
    for i in range(height):
        for j in range(width):
            if (board[i][j] == alive):
                rowStr += "@"
            else:
                rowStr += " "
        rowStr += "\n"

    print(rowStr)

def updateBoard(board):
    # updateBoard will update every cell according to the 4 rules
    # parameter board is just a list of lists
    updatedBoard = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighborSum = 0


printBoard(deadState)
printBoard(randomState)
log.close()
