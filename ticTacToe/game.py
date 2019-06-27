import tttFunctions as tFn
import strFile
import copy

tFn.getPlayerNames(tFn.playerList)
currentBoard = tFn.currentBoard
exit = False
i = 0
while not exit:
    move = tFn.getTurn(tFn.playerList[i])
    turn = tFn.updateBoard(currentBoard, i, move[1])
    currentBoard = turn[0]
    updateOccurred = turn[1]
    tFn.printBoard(currentBoard)
    test = tFn.checkBoard(currentBoard)
    exit = test[0]
    winner = test[1]
    if test[0] and winner == None:
        strFile.announceDraw
    if winner != None:
        print(strFile.announceWin(winner))
        exit = True
    # complicated until Ai built in
    if updateOccurred:
        if i == 0 and len(tFn.playerList) == 2:
            i = 1
        else:
            i = 0



