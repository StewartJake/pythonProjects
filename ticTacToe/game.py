import copy
import pdb
import gameAi
import tttFunctions as tFn
import strFile

#tFn.getPlayerNames(tFn.playerList)
randall = gameAi.Ai("O", gameAi.randomAi, "RANDall")
jaime = gameAi.Ai("O", gameAi.findWinningAi, "jAIme")
aida = gameAi.Ai("O", gameAi.findWinLossAi, "AIda")
raiden = gameAi.Ai("X", gameAi.minimaxAi, "rAIden")
tFn.playerList[0] = raiden 
#tFn.playerList.append(raiden) 
tFn.playerList.append(randall)
def playGame(playerList):
    exit = False
    currentBoard = tFn.currentBoard
    i = 0
    while not exit:
        if type(playerList[i]) == gameAi.Ai:
            move = playerList[i].choose(currentBoard)
        else:
            move = tFn.getTurn(currentBoard, playerList[i])
        if i == 0:
            symbol = "X"
        else:
            symbol = "O"
        currentBoard = tFn.updateBoard(currentBoard, symbol, move)
        tFn.printBoard(currentBoard)
        test = tFn.checkBoard(currentBoard, symbol)
        exit, won, score = test
        if test[0] and won == False:
            print(strFile.announceDraw)
        if won:
            if type(playerList[i]) != gameAi.Ai:
                print(strFile.announceWin(playerList[i]))
            else:
                print(strFile.announceWin(playerList[i].name))
            return i
            exit = True
        if i == 0:
            i = 1
        else:
            i = 0


def statTest():
    p1Wins = 0
    p2Wins = 0
    for i in range(100):
        winner = playGame(tFn.playerList)
        if winner == 0:
            p1Wins += 1
        elif winner == 1:
            p2Wins += 1
    print("Player1: " + str(p1Wins))
    print("Player2: " + str(p2Wins))

testBoard = [["X","O","X"],
            ["O", "O","X"],
            ["X","O","O"]];
#playGame(tFn.playerList)
statTest()
