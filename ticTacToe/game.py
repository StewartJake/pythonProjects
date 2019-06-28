import tttFunctions as tFn
import strFile
import copy
f = open("log", "a+")
tFn.getPlayerNames(tFn.playerList)
currentBoard = tFn.currentBoard
exit = False
i = 0
while not exit:
    move = tFn.getTurn(tFn.playerList[i], currentBoard)
    f.write(move + '\n')
    currentBoard = tFn.updateBoard(currentBoard, i, move)
    tFn.printBoard(currentBoard)
    test = tFn.checkBoard(currentBoard)
    exit, winner = test
    if test[0] and winner == None:
        print(strFile.announceDraw)
    if winner != None:
        print(strFile.announceWin(winner))
        exit = True
    if i == 0:
        i = 1
    else:
        i = 0

f.close()

