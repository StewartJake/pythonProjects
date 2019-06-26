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
# Player names
try:
    players = int(input(strFile.getPlayerNum))
    if not players in (1,2):
        print(strFile.tooManyPlayers)
        sys.exit()
except ValueError:
    print(strFile.valErrInt)
    sys.exit()
playerList = [""]*players
for i,player in enumerate(playerList):
    playerList[i] = input(strFile.getPlayerName(i+1))
player1 = playerList[0]
if players == 2:
    player2 = playerList[1]

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
    updatedBoard[dict[choice][0]][dict[choice][1]] = symbol
    return updatedBoard

nextBoard = updateBoard(startingBoard, 0, '9')
printBoard(nextBoard)
nextBoard = updateBoard(nextBoard, 1, '8')
printBoard(nextBoard)
currentBoard = updateBoard(nextBoard, 0, '7')
printBoard(nextBoard)
getTurn(player1)
# TODO Check board
# TODO Decide winner/draw
