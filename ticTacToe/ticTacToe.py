#ticTacToe.py
# A terminal tic tac toe

import strFile
import sys
import copy

# Create board
startingBoard = [[None]*3 for _ in range(3)]
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
            formatted += str(board[r][c]) + strFile.colMarker
        formatted += "\n" + rw
    print(formatted)

    
# TODO Get player turn
def getTurn(player):
    print(strFile.turnAlert(player))
    choice = input(strFile.validOptions)
    while (choice.lower() != "map"
            and not any(choice in rowList for rowList in tutorialBoard)):
        choice = input(strFile.validOptions)
    
getTurn(player1)
# TODO Update board
# TODO Check board
# TODO Decide winner/draw
