import gameAi


x1Away = [['X','O','O'],['X','X','O'],[None, None, None]]
o1Away = [['O','O','X'],['O','X','O'],[None, 'X', None]]
x2Away = [[None,'O',None], ['X','X','O'], [None, 'X', None]]
x1Space = [['X','O','O'],['X','O','O'],[None,'X','X']]
xWin = [['X','X','X'],[None,None,None],[None,None,None]]
oWins =[['O','O','O'],[None,None,None],[None,None,None]] 

def tests():
    print("-X    True")
    print(gameAi.minimaxScore(o1Away, "X", True))
    print("X    False")
    print(gameAi.minimaxScore(o1Away, "X", False))
    print("O    True")
    print(gameAi.minimaxScore(o1Away, "O", True))
    print("-O    False")
    print(gameAi.minimaxScore(o1Away, "O", False))

