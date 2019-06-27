#ticTacToe.py
# A terminal tic tac toe

import strFile
import sys
import copy

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
def getTurn(player):
    # argument is a players name
    # Returns a tuple with the player and the board index
    print(strFile.turnAlert(player))
    choice = input(strFile.validOptionStr)
    dict = strFile.choiceMap
    # Verify input to be [map] or in [1,9]
    while ((not choice.lower() in strFile.validOptions
            and not any(choice in rowList for rowList in tutorialBoard))
        or choice.lower() in strFile.validOptions 
        or currentBoard[dict[choice][0]][dict[choice][1]] != None):
        # Ensures choice only goes out to return as an int
        # map
        if choice.lower() == strFile.validOptions[0]:
            printBoard(tutorialBoard)
        # board
        elif choice.lower() == strFile.validOptions[1]:
            printBoard(currentBoard)
        choice = input(strFile.validOptionStr)
    return(player, choice) 


# Update board
def updateBoard(board, player, choice):
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
    cell = updatedBoard[dict[choice][0]][dict[choice][1]]
    if updatedBoard[dict[choice][0]][dict[choice][1]] == None:
        updatedBoard[dict[choice][0]][dict[choice][1]]= symbol
        updated = True
    return (updatedBoard, updated)


# Check board
def checkBoard(board):
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
    if (board[0][0] == symbol and board[2][2] == symbol
        and board[0][2] == symbol and board[2][0] == symbol):
        if symbol == "X":
            winner = playerList[0]
        elif symbol == "O":
            winner = playerList[1]
    return (full, winner)
