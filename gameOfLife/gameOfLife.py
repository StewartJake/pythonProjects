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

def findNeighbors(board):
    #board will be a list and this function will return a sum of neighbors
    neighborBoard = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighborSum = 0
            #concern is for hitting the left index
            #right overflow has no effect in slices
            if (i > 0) and (i < len(board) - 1):
                #central cell
                if (j > 0) and (j < len(board[i]) - 1):
                    neighborSum += board[i-1][j-1:j+2].count(alive)
                    neighborSum += board[i][j-1]
                    neighborSum += board[i][j+1]
                    neighborSum += board[i+1][j-1:j+2].count(alive)
                #left-border cell
                elif (j == 0):
                    neighborSum += board[i-1][j:j+2].count(alive)
                    neighborSum += board[i][j+1]
                    neighborSum += board[i+1][j:j+2].count(alive)
                #right-border cell
                elif (j == len(board[i]) - 1):
                    neighborSum += board[i-1][j-1:j+1].count(alive)
                    neighborSum += board[i][j-1]
                    neighborSum += board[i+1][j-1:j+1].count(alive)
            elif (i == len(board) - 1):
                #bottom-border
                if (j > 0) and (j < len(board[i]) - 1) :
                    neighborSum += board[i-1][j-1:j+2].count(alive)
                    neighborSum += board[i][j-1]
                    neighborSum += board[i][j+1]
                #south-west cell
                elif (j == 0):
                    neighborSum += board[i-1][j:j+2].count(alive)
                    neighborSum += board[i][j+1]
                #south-east cell
                elif (j == len(board[i]) - 1):
                    neighborSum += board[i-1][j-1:j+1].count(alive)
                    neighborSum += board[i][j-1]
            elif (i == 0):
                #top-border
                if (j > 0) and (j < len(board[i]) - 1) :
                    neighborSum += board[i+1][j-1:j+2].count(alive)
                    neighborSum += board[i][j-1]
                    neighborSum += board[i][j+1]
                #north-west cell
                elif (j == 0):
                    neighborSum += board[i+1][j:j+2].count(alive)
                    neighborSum += board[i][j+1]
                #north-east cell
                elif (j == len(board[i]) - 1):
                    neighborSum += board[i+1][j-1:j+1].count(alive)
                    neighborSum += board[i][j-1]
            neighborBoard[i][j] = neighborSum
    return neighborBoard

printBoard(randomState)
# pretty print b/c hard to confirm in errorLog
a = findNeighbors(randomState)
rowStr = ""
for i in range(len(a)):
    for j in range(len(a[i])):
        rowStr += str(a[i][j])
    rowStr += "\n"

print(rowStr)
log.close()
