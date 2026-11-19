Grid = [
    ["S", 1, 3],
    [3, 2, 1],
    [2, 3, "G"]
]

Rows = len(Grid)
Columns = len(Grid[0])
Route = []

total_nodes = Rows * Columns
row = 0
column = 0
NodeWeight = Grid[row][column] # current weight
Visited = []
Table = {}

i = 0
j = 0

S = [0, 0]
G = [0, 0]

def getWeight(Row, Column): # for any other weight
    if Grid[Row][Column] == "S" or Grid[Row][Column] == "G":
        return 1
    else:
        return Grid[Row][Column]

# map all to the table
while i < total_nodes:
    column = 0
    while column < Columns:
        row = 0
        while row < Rows:
            Table[str(row)+","+str(column)] = [0, ""]
            row += 1
            i += 1
        column += 1


i = 0
row = 0
column = 0
while i < total_nodes: # loop runs inf
    while row < Rows: 
        if getWeight(row, column) == "S":
            Table[str(row)+""+str(column)] = [0, ""]
        if getWeight(row + 1, column) < (getWeight(row - 1, column) and getWeight(row, column + 1) and getWeight(row, column - 1)): # right
            if [row + 1, column] not in Visited:
                row += 1
                Visited.append([row, column])
            Table[str(row)+""+str(column)] = [NodeWeight]
        elif getWeight(row - 1, column) < (getWeight(row + 1, column) and getWeight(row, column + 1) and getWeight(row, column - 1)): # left
            if [row -1, column] not in Visited:
                row -= 1
                Visited.append([row, column])
            Table[str(row)+""+str(column)] = [NodeWeight]
        elif getWeight(row, column + 1) < (getWeight(row + 1, column) and getWeight(row - 1, column) and getWeight(row, column - 1)): # up
            if [row, column + 1] not in Visited:
                column += 1
                Visited.append([row, column])
            Table[str(row)+""+str(column)] = [NodeWeight]
        elif getWeight(row, column - 1) < (getWeight(row + 1, column) and getWeight(row, column + 1) and getWeight(row - 1, column)): # down
            if [row, column - 1] not in Visited:
                column -= 1
                Visited.append([row, column])
            Table[str(row)+""+str(column)] = [NodeWeight]
        
print(Table)


        
print(Table)
