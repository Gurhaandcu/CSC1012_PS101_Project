import sys

Grid = [
    ["S", 3, 3],
    [3, 2, 1],
    [2, 3, "G"]
]

Rows = len(Grid)
Columns = len(Grid[0])
Route = []


total_nodes = Rows * Columns
row = 0
column = 0
Visited = []
Table = {}

i = 0
j = 0

S = [-1, -1]
G = [-1, -1]

def getPure(Row, Column): # For Pure value representative of the node
    return Grid[Row][Column]


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
            if getPure(row, column) == "S":
                Table[str(row)+","+str(column)] = [1, ""]
                S = [row, column]
            elif getPure(row, column) == "G":
                Table[str(row)+","+str(column)] = [1, ""]
                G = [row, column]
            else:
                Table[str(row)+","+str(column)] = [getPure(row, column), ""]
            row += 1
            i += 1
        column += 1

if S == [-1, -1] or G == [-1, -1]:
    sys.exit("No S or G exists")

# 100% works upto here

print(Table)

# here is dijkstra's algorithm:
i = 0
row = S[0]
column = S[1]
Visited.append([row, column])

while getPure(row, column) != "G": 
    if (getWeight(row + 1, column) <= (getWeight(row - 1, column) and getWeight(row, column + 1) and getWeight(row, column - 1))) and getWeight(row + 1, column) not in Visited: # right
        row += 1 # Goes to next node
        Visited.append([row, column]) # adds to visited
        Table[str(row)+","+str(column)][1] = [str(row-1)+""+str(column)] # marks the previous node in the table for this node

    elif (getWeight(row - 1, column) <= (getWeight(row + 1, column) and getWeight(row, column + 1) and getWeight(row, column - 1))) and getWeight(row - 1, column) not in Visited: # left
        row -= 1 # Goes to next node
        Visited.append([row, column]) # adds to visited
        Table[str(row)+","+str(column)][1] = [str(row+1)+""+str(column)] # marks the previous node in the table for this node

    elif (getWeight(row, column + 1) <= (getWeight(row + 1, column) and getWeight(row - 1, column) and getWeight(row, column - 1))) and getWeight(row, column + 1) not in Visited: # up
        column += 1 # Goes to next node
        Visited.append([row, column]) # adds to visited
        Table[str(row)+","+str(column)][1] = [str(row)+""+str(column-1)] # marks the previous node in the table for this node

    elif (getWeight(row, column - 1) <= (getWeight(row + 1, column) and getWeight(row, column + 1) and getWeight(row - 1, column))) and getWeight(row, column - 1) not in Visited: # down
        column -= 1 # Goes to next node
        Visited.append([row, column]) # adds to visited
        Table[str(row)+","+str(column)][1] = [str(row)+""+str(column+1)] # marks the previous node in the table for this node
print(Table)
