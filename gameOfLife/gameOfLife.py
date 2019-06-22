import random
import pdb

log = open("errorLog","w+")

height = 5;
width = 5;
alive = 1;
dead = 0;

# a tuple of tuples with dim width x height
deadState = [[dead]*width for _ in range(height)]

#pdb.set_trace();
# randomize the boardState
randomState = deadState;
for i in range(height):
    for j in range(width):
        randomState[i][j] = random.randint(0,1);

# print board state like a board
rowStr = ""
for i in range(height):
    for j in range(width):
        if (randomState[i][j] == alive):
            rowStr += "@";
        else:
            rowStr += " ";
    rowStr += "\n";

print(randomState, file = log);


print(rowStr);

log.close();
