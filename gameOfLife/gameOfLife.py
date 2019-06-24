import random
import copy
import pdb
import sys

ALIVE = 1
DEAD = 0

log = open("errorLog","w+")
saveLog = open("saves","r")
height = 38 
width = 150
# a tuple of tuples with dim width x height
deadState = [[DEAD]*width for _ in range(height)]

# randomize the boardState
randomState = copy.deepcopy(deadState)

for i in range(height):
    for j in range(width):
        randomState[i][j] = random.randint(0,1)
def  printBoard(board):
    # print board state like a board
    rowStr = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == ALIVE):
                rowStr += u"\u2588" 
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
    ALIVE = 1
    DEAD = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighborSum = 0
            #concern is for hitting the left index
            #right overflow has no effect in slices
            if (i > 0) and (i < len(board) - 1):
                #central cell
                if (j > 0) and (j < len(board[i]) - 1):
                    neighborSum += board[i-1][j-1:j+2].count(ALIVE)
                    neighborSum += board[i][j-1]
                    neighborSum += board[i][j+1]
                    neighborSum += board[i+1][j-1:j+2].count(ALIVE)
                #left-border cell
                elif (j == 0):
                    neighborSum += board[i-1][j:j+2].count(ALIVE)
                    neighborSum += board[i][j+1]
                    neighborSum += board[i+1][j:j+2].count(ALIVE)
                #right-border cell
                elif (j == len(board[i]) - 1):
                    neighborSum += board[i-1][j-1:j+1].count(ALIVE)
                    neighborSum += board[i][j-1]
                    neighborSum += board[i+1][j-1:j+1].count(ALIVE)
            elif (i == len(board) - 1):
                #bottom-border
                if (j > 0) and (j < len(board[i]) - 1) :
                    neighborSum += board[i-1][j-1:j+2].count(ALIVE)
                    neighborSum += board[i][j-1]
                    neighborSum += board[i][j+1]
                #south-west cell
                elif (j == 0):
                    neighborSum += board[i-1][j:j+2].count(ALIVE)
                    neighborSum += board[i][j+1]
                #south-east cell
                elif (j == len(board[i]) - 1):
                    neighborSum += board[i-1][j-1:j+1].count(ALIVE)
                    neighborSum += board[i][j-1]
            elif (i == 0):
                #top-border
                if (j > 0) and (j < len(board[i]) - 1) :
                    neighborSum += board[i+1][j-1:j+2].count(ALIVE)
                    neighborSum += board[i][j-1]
                    neighborSum += board[i][j+1]
                #north-west cell
                elif (j == 0):
                    neighborSum += board[i+1][j:j+2].count(ALIVE)
                    neighborSum += board[i][j+1]
                #north-east cell
                elif (j == len(board[i]) - 1):
                    neighborSum += board[i+1][j-1:j+1].count(ALIVE)
                    neighborSum += board[i][j-1]
            neighborBoard[i][j] = neighborSum
    return neighborBoard

def updateBoard(board):
    nextBoard = copy.deepcopy(board)
    neighBoard = findNeighbors(board)
#    pdb.set_trace();
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            #over/under-population
            if (board[i][j] == ALIVE) and ((neighBoard[i][j] <= 1) or (neighBoard[i][j] > 3)):
                    nextBoard[i][j] = DEAD
            #reporduction
            if (board[i][j] == DEAD) and (neighBoard[i][j] == 3):
                    nextBoard[i][j] = ALIVE
    return nextBoard

def loadBoard(key):
    # take a key, as a string, to search the save file
    # returns a tuple whether it was found and if so also a board
    found = False
    f = open("saves","r")
    lineList = f.readlines()
    board = [[]]
#    pdb.set_trace()
    for line in lineList:
        if (not line.startswith("#") and key in line):
            ind = lineList.index(line)
            board = lineList[ind + 1].split('\n')      #relies on each line having an eol
            found = True
    return (found, eval(board[0]))

# attempts to end program if just stuck in same pattern
#still needs work
formerState = copy.deepcopy(deadState)
formerState2 = copy.deepcopy(formerState)
i = 0
# add some sanitation to this input
initialState = randomState
wantLoaded = input("Do you want to load a file?" + '\n' + "(Y/N):\n")
if (wantLoaded.lower() == "y"):
    boardChoice = input("What is the save file:\n")
    gameStart = loadBoard(boardChoice)
    if (gameStart[0]):
        initialState = gameStart[1]
    else:
        print("Board not found in save file.")
        sys.exit()

while ((initialState != formerState) and (initialState != formerState2)):
    formerState = initialState
    if (i%2 ==1):
        formerstate2 = initialState
#    pdb.set_trace()
    initialState = updateBoard(initialState)
    print(initialState,file = log)
    printBoard(initialState)
    i += 1

log.close()
