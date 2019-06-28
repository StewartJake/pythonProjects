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

