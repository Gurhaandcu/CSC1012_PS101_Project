import sys
from collections import deque

# Read input
Rows, Columns, K = map(int, input().split())

Grid = []
i = 0

while i < Rows:
    Grid.append(list(input().strip()))
    i += 1

Table = {}
S = [-1, -1]
G = [-1, -1]

StaminaCost = {
    "F": 2,
    "M": 3
}

Directions = [ # up / down / left / right
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]

def getPure(Row, Column):
    return Grid[Row][Column]

def getWeight(Row, Column):
    return StaminaCost.get(Grid[Row][Column], 1)

# Fill dictionairy
row = 0
while row < Rows:
    column = 0
    while column < Columns:
        if getPure(row, column) == "S":
            S = [row, column]

        elif getPure(row, column) == "G":
            G = [row, column]

        Table[str(row)+","+str(column)] = [
            float("inf"),
            float("inf"),
            ""
        ]
        column += 1
    row += 1

# check if start and end exist
if S == [-1, -1] or G == [-1, -1]:
    sys.exit("No S or G exists")


# starting pos
StartKey = str(S[0])+","+str(S[1])
Table[StartKey] = [1, 0, ""]

# create queue
Updated = deque()
Updated.append((S[0], S[1]))

InQueue = set()
InQueue.add((S[0], S[1]))

# Find best route
while len(Updated) > 0:
    Current = Updated.popleft()
    InQueue.remove(Current)
    row = Current[0]
    column = Current[1]
    CurrentKey = str(row)+","+str(column)
    CurrentDays = Table[CurrentKey][0]
    CurrentStamina = Table[CurrentKey][1]

    d = 0
    while d < 4:
        NewRow = row + Directions[d][0]
        NewColumn = column + Directions[d][1]
        if NewRow >= 0 and NewRow < Rows and NewColumn >= 0 and NewColumn < Columns:
            if Grid[NewRow][NewColumn] != "#":
                NeighbourKey = str(NewRow)+","+str(NewColumn)
                NeighbourWeight = getWeight(NewRow, NewColumn)
                if NeighbourWeight <= K:
                    NewDays = CurrentDays
                    NewStamina = CurrentStamina + NeighbourWeight
                    if NewStamina > K:
                        NewDays += 1
                        NewStamina = NeighbourWeight
                    NewTime = (NewDays, NewStamina)
                    OldTime = (
                        Table[NeighbourKey][0],
                        Table[NeighbourKey][1]
                    )

                    if NewTime < OldTime:
                        Table[NeighbourKey][0] = NewDays
                        Table[NeighbourKey][1] = NewStamina
                        Table[NeighbourKey][2] = CurrentKey
                        Neighbour = (NewRow, NewColumn)
                        if Neighbour not in InQueue:
                            Updated.append(Neighbour)
                            InQueue.add(Neighbour)
        d += 1

# ans
GoalKey = str(G[0])+","+str(G[1])
if Table[GoalKey][0] == float("inf"):
    print(-1)
else:
    print(Table[GoalKey][0])
