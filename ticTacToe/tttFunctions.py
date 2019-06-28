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
    for i,player in enumerate(playerList):
        playerList[i] = input(strFile.getPlayerName(i+1))
    if playerNum == 1:
        playerList.append("AI")

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
def getTurn(player, board):
    # Fn: get's a players move and determines if it is allowable
    # Argument: players name as string, board as list of list
    # Returns the players choice as an int from 1-9 
    legal = False
    if player != "AI":
        print(strFile.turnAlert(player))
    else:
        choice = gameAi.randomAi(board, "O")
        legal = True
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


def updateBoard(board, player, choice):
    # Fn: given he arguments this function will update the board
    # Argument: board is a list of lists board, player is going to
    # be the index of the player, choice is the index of the cell
    # the player chose
    # Return: a new board updated to reflect choice
    updatedBoard = copy.deepcopy(board)
    # The indexing became rough as I tried to make it cleaner for the
    # user and this dictionary should map choice to [r][c]
    dict = strFile.choiceMap
    if player == 0:
        symbol = "X"
    else:
        symbol = "O"
    updated = False
    # tried to assign a var to simplify | failed
    # look into why later
    if updatedBoard[dict[choice][0]][dict[choice][1]] == None:
        updatedBoard[dict[choice][0]][dict[choice][1]]= symbol
        updated = True
    return updatedBoard


def checkBoard(board):
    # Fn: checks whether the board is full and if any win conditions
    # are met
    # Arguments: board representted by a list of lists
    # Returns a tuple with a boolean as to whether the board is full
    # and either a winner or None
    if any(None in row for row in board):
        full = False
    else:
        full = True
    winner = None
    # Rows
    for r in range(len(board)):
        symbol = board[r][0]
        if board[r][1] == symbol and board[r][2] == symbol:
            if symbol == "X":
                winner = playerList[0]
            elif symbol == "O":
                winner = playerList[1]
    # Columns
    for r in range(len(board)):
        for c in range(len(board[r])):
            symbol = board[0][c]
            if board[1][c] == symbol and board[2][c] == symbol:
                if symbol == "X":
                    winner = playerList[0]
                elif symbol == "O":
                    winner = playerList[1]
    # Diagonals
    # Adjust later if want non-traditional board sizes
    symbol = board[1][1]
    if ((board[0][0] == symbol and board[2][2] == symbol)
        or (board[0][2] == symbol and board[2][0] == symbol)):
        if symbol == "X":
            winner = playerList[0]
        elif symbol == "O":
            winner = playerList[1]
    return (full, winner)
