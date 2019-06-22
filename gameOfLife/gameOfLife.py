import random

log = open("errorLog","w+")

height = 5
width = 5

# a tuple of tuples with dim width x height
deadState = (((0,)*width),)*height

randomState = deadState
for i in range(height):
    for j in range(width):
        randomState[i][j] = random.randint(0,1)

print(randomState, file = log)

