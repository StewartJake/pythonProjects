import copy
import pdb
import gameAi
import tttFunctions as tFn
import strFile

tFn.getPlayerNames(tFn.playerList)
randoRandall = gameAi.Ai("X", gameAi.randomAi, "RANDall")
jaime = gameAi.Ai("O", gameAi.findWinningAi, "jAIme")
aida = gameAi.Ai("O", gameAi.findWinLossAi, "AIda")
#tFn.playerList[0] = randoRandall 
tFn.playerList.append(randoRandall) 

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
        exit, won = test
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


def test():
    p1Wins = 0
    p2Wins = 0
    for i in range(10000):
        winner = playGame(tFn.playerList)
        if winner == 0:
            p1Wins += 1
        elif winner == 1:
            p2Wins += 1
    print("Player1: " + str(p1Wins))
    print("Player2: " + str(p2Wins))


playGame(tFn.playerList)
#test()
