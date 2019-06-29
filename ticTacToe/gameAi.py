import random
import math
import pdb
import tttFunctions as tFn
import strFile


class Ai:
    
    def __init__(self, symbol, algo, name):
        self.symbol = symbol
        self.func = algo
        self.name = name

    def choose(self, board):
        return self.func(board, self.symbol)

# All the AI functions will take in 2 arguments:
# board and symbol of the person who's turn it is
# Return will be the coordinate of the move


def legalMoves(board):
    # Determines what cells are available on a board
    # Arguments: board as list of list
    # Return: a list of open cells
    legalMoves = [];
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == None:
                for key, val in strFile.choiceMap.items():
                    if val == (r, c):
                        legalMoves.append(key)
                        break
    return legalMoves


#def minimaxAi(board, symbol):
#   bestMoves 

def minimaxScore(board, symbol, isMaximizer):
    # Runs the minimax algorithm
    results = tFn.checkBoard(board, symbol)
    full = results[0]
    won = results[1]
    score = results[2]
    moveSet = legalMoves(board)
    if symbol == "X":
        minPlayer = "O"
    else:
        minPlayer = "X"
    # Base Case
    if won or full:
        return score
    elif isMaximizer:
        highScore = -(math.inf)
        for move in moveSet:
            newBoard = tFn.updateBoard(board, symbol, move)
            tempScore = minimaxScore(newBoard, symbol, True)
            highScore = max(highScore, tempScore)
        return highScore
    else:
        lowScore = math.inf
        for move in moveSet:
            newBoard = tFn.updateBoard(board, symbol, move)
            tempScore = minimaxScore(newBoard, minPlayer, False)
            lowScore = min(lowScore, tempScore)
        return lowScore

def randomAi(board, symbol):
    # Randomly chooses an open space
    possibleMoves = legalMoves(board)
    choice = random.randrange(0, len(possibleMoves))
    return possibleMoves[choice]


def showWinningMoves(board, symbol):
    # Function: show winning cells
    # Argument: board as a list of lists
    # Return: a list of possible winning cells (1-9) index
    openCells = legalMoves(board)
    winningMoves = []
    # Rows
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[0][c] == symbol and board[1][c] == symbol:
                if tFn.coordsToMap(2,c)  in openCells:
                    winningMoves.append((2,c))
            elif board[0][c] == symbol and board[2][c] == symbol:
                if tFn.coordsToMap(1, c) in openCells:
                    winningMoves.append((1,c))
            elif board[1][c] == symbol and board[2][c] == symbol:
                if tFn.coordsToMap(0, c) in openCells:
                    winningMoves.append((0,c))
    # Columns
    for r in range(len(board)):
        if board[r][0] == symbol and board[r][1] == symbol:
            if tFn.coordsToMap(r, 2) in openCells:
                winningMoves.append((r,2))
        elif board[r][1] == symbol and board[r][2] == symbol:
            if tFn.coordsToMap(r, 0) in openCells:
                winningMoves.append((r,0))
        elif board[r][0] == symbol and board[r][2] == symbol:
            if tFn.coordsToMap(r, 1) in openCells:
                winningMoves.append((r,1))
    # Diagonals
    if board[1][1] == symbol:
        if board[0][0] == symbol and tFn.coordsToMap(2, 2) in openCells: 
            winningMoves.append((2,2))
        elif board[2][2] == symbol and tFn.coordsToMap(0, 0) in openCells:
            winningMoves.append((0,0))
        elif board[2][0] == symbol and tFn.coordsToMap(0, 2) in openCells:
            winningMoves.append((0,2))
        elif board[0][2] == symbol and tFn.coordsToMap(2, 0) in openCells:
            winningMoves.append((2,0))
    return winningMoves


def findWinningAi(board, symbol):
    # If a winning space is open, will choose it. Random otherwise
    winningMoves = showWinningMoves(board, symbol) 
    if len(winningMoves) > 0:
        for key, val in strFile.choiceMap.items():
            if val == winningMoves[0]:
                choice = key
                break
    else:
        choice = randomAi(board, symbol)
    return choice
        

def findWinLossAi(board, symbol):
    # Will claim a winning spot or block a losing spot.
    # Random otherwise
    if symbol == "X":
        otherSymbol = "O"
    else:
        otherSymbol = "X"
    myWinningMoves = showWinningMoves(board, symbol)
    otherWinningMoves = showWinningMoves(board, otherSymbol)
    if len(myWinningMoves) > 0:
        for key, val in strFile.choiceMap.items():
            if val == myWinningMoves[0]:
                choice = key
                break
    elif len(otherWinningMoves) > 0:
        for key, val in strFile.choiceMap.items():
            if val == otherWinningMoves[0]:
                choice = key
                break
    else:
        choice = randomAi(board, symbol);
    return choice


