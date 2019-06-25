# A file of strings and fns to return formatted strings
# Probably unnecessary for a program this size
greeting = "Hello and welcome!"
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
