#ticTacToe.py
# A terminal tic tac toe

import strFile
import sys

# Create board
startingBoard = [[" "]*3 for _ in range(3)]
i = 1
for r in range(len(startingBoard)):
    for c in range(len(startingBoard[r])):
        startingBoard[r][c] = str(i)
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


#  Print board
def printBoard(board):
    rw = strFile.rowStr 
    formatted = rw 
    for r in range(len(board)):
        formatted += strFile.colMarker
        for c in range(len(board[r])):
            formatted += board[r][c] + strFile.colMarker
        formatted += "\n" + rw
    print(formatted)


printBoard(startingBoard)
# TODO Update board
# TODO Check board
# TODO Name winner
