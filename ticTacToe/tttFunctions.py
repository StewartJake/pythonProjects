#ticTacToe.py
# A terminal tic tac toe

import strFile
import sys
import copy
import gameAi
import pdb

# Create board
startingBoard = [[None]*3 for _ in range(3)]
currentBoard = copy.deepcopy(startingBoard)
tutorialBoard = copy.deepcopy(startingBoard)
i = 1
for r in range(len(tutorialBoard)):
    for c in range(len(tutorialBoard[r])):
        tutorialBoard[r][c] = str(i)
        i += 1
playerList = [""]


def coordsToMap(x, y = None):
    # Function: converts between coords and mapping
    # Args: can be passed one str as a map or 2 integers as coords
    # Return: if given a str returns a tuple of coords if coords a
    #         str
    if y == None:
        return strFile.choiceMap[str(x)]
    else:
        tpl = tuple([x, y])
        for key, val in strFile.choiceMap.items():
            if val == tpl:
                return key



# Player names
def getPlayerNames(playerList):
    try:
        playerNum = int(input(strFile.getPlayerNum))
        if not playerNum in (1,2):
            print(strFile.tooManyPlayers)
            sys.exit()
    except ValueError:
        print(strFile.valErrInt)
        sys.exit()
    if playerNum == 2:
        playerList.append("")
    for i,player in enumerate(playerList):
        playerList[i] = input(strFile.getPlayerName(i+1))

#  Print board
def printBoard(board):
    rw = strFile.rowStr 
    formatted = rw 
    for r in range(len(board)):
        formatted += strFile.colMarker
        for c in range(len(board[r])):
            if board[r][c] == None:
                outStr = " "
            else:
                outStr = str(board[r][c])
            formatted += outStr + strFile.colMarker
        formatted += "\n" + rw
    print(formatted)

    
# Get player turn
def getTurn(board, player):
    # Fn: get's a players move and determines if it is allowable
    # Argument: players name as string, board as list of list
    # Returns the players choice as an int from 1-9 
    legal = False
    while not legal:
        choice = input(strFile.validOptionStr)
        dict = strFile.choiceMap
        # Verify input to be [map] or in [1,9]
        while ((not choice.lower() in strFile.validOptions
                and not any(choice in rowList
                        for rowList in tutorialBoard))
            or choice.lower() in strFile.validOptions 
            or currentBoard[dict[choice][0]][dict[choice][1]] != None):
            # Ensures choice only goes out to return as an int
            # map
            if choice.lower() == strFile.validOptions[0]:
                printBoard(tutorialBoard)
            # board
            elif choice.lower() == strFile.validOptions[1]:
                printBoard(board)
            choice = input(strFile.validOptionStr)
        # tried to assign a var to simplify | failed
        # look into why later
        if board[dict[choice][0]][dict[choice][1]] == None:
            legal = True
        else:
            print(strFile.spaceFilled)
    return choice 


def updateBoard(board, symbol, choice):
    # Fn: given he arguments this function will update the board
    # Argument: board is a list of lists board, player is going to
    # be the index of the player, choice is the index of the cell
    # the player chose
    # Return: a new board updated to reflect choice
    updatedBoard = copy.deepcopy(board)
    # The indexing became rough as I tried to make it cleaner for the
    # user and this dictionary should map choice to [r][c]
    dict = strFile.choiceMap
    updated = False
    # tried to assign a var to simplify | failed
    # look into why later
    if updatedBoard[dict[choice][0]][dict[choice][1]] == None:
        updatedBoard[dict[choice][0]][dict[choice][1]]= symbol
        updated = True
    return updatedBoard


def checkBoard(board, symbol):
    # Fn: checks whether the board is full and if any win conditions
    # are met. 
    # Arguments: board represented by a list of lists
    # Returns a tuple with a boolean as to whether the board is full
    # and whether the game has been won
    if any(None in row for row in board):
        full = False
    else:
        full = True
    won = None 
    score = None
    # Rows
    for r in range(len(board)):
        if (board [r][0] ==  board[r][1]
            and board[r][0] == board[r][2]
            and board[r][0] != None):
            if board[r][0] == symbol:
                won = True
            else:
                won = False
    # Columns
    for r in range(len(board)):
        for c in range(len(board[r])):
            if (board [0][c] == board[1][c]
                and board[0][c] == board[2][c] 
                and board[0][c] != None):
                if board[0][c] == symbol:
                    won = True
                else:
                    won = False
    # Diagonals
    if board[1][1] != None:
        if ((board[0][0] == board[1][1] and board[1][1] == board[2][2])
            or (board[0][2] == board[1][1] and board[1][1] == board[2][0])):
                if board[1][1] == symbol:
                    won = True
                else:
                    won = False
    return (full, won)
