import tttFunctions
import random
import strFile
import pdb

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


def randomAi(board, symbol):
    possibleMoves = legalMoves(board)
    choice = random.randrange(0, len(possibleMoves))
    return possibleMoves[choice]


def findWinningAi(board, symbol):
    winningMoves = [] 
    # Rows
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[0][c] == symbol and board[1][c] == symbol:
                winningMoves.append((2,c))
            elif board[0][c] == symbol and board[2][c] == symbol:
                winningMoves.append((1,c))
            elif board[1][c] == symbol and board[2][c] == symbol:
                winningMoves.append((0,c))
    # Columns
    for r in range(len(board)):
        if board[r][0] == symbol and board[r][1] == symbol:
            winningMoves.append((r,2))
        elif board[r][1] == symbol and board[r][2] == symbol:
            winningMoves.append((r,0))
        elif board[r][0] == symbol and board[r][2] == symbol:
            winningMoves.append((r,1))
    # Diagonals
    if board[1][1] == symbol:
        if board[0][0] == symbol:
            winningMoves.append((2,2))
        elif board[2][2] == symbol:
            winningMoves.append((0,0))
        elif board[2][0] == symbol:
            winningMoves.append((0,2))
        elif board[0][2] == symbol:
            winningMoves.append((2,0))
    if len(winningMoves) > 0:
        for key, val in strFile.choiceMap.items():
            if val == winningMoves[0]:
                choice = key
                break
    else:
        choice = randomAi(board, symbol)
    return choice
        
