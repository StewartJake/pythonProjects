# A file of strings and fns to return formatted strings
# Probably unnecessary for a program this size
getPlayerNum = """Choose a mode:
    [1] Single Player
    [2] Multi Player
    Please type 1 or 2.\n"""
valErrInt = "Input must be an integer!"
def getPlayerName(number):
    # Number is the players number
    # Returns a string stating number while asking for name
    return "What is player " + str(number) + "\'s name?\n"
rowMarker = "-"
rowStr = " " + rowMarker*5 + " \n"
colMarker = "|"
tooManyPlayers = "Only 1 or 2 players are allowed at one time!"
instructions = """
Hello and welcome!
The objective is to get 3 in a row, 3 in a column, or 3
diagonally. Players will take turns picking cells on the board 
until one player wins or both draw.
The players pick cells [1-9] like the map below:"""
#pretty print tutorial board after instructions
def turnAlert(playersName):
    return "What is your move, " + playersName + ".\n"
validOptions = """Valid options include digits [1-9] or [map],
which opens the index map.\n""" 
