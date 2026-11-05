n = int(input("Please enter the number of rows: ")) # num of rows
m = int(input("Please enter the number of columns: ")) # num of columns
k = int(input("Please enter your stamina: ")) # stamina
i = 0
j = 0
map = []
grid = []
temp = []
key = ["S", ".", "F", "M", "#", "G"]
days = 0

while n < 1:
    n = int(input("Please re-enter the number of rows: "))

while m > 50:
    m = int(input("Please re-enter the number of columns: "))

while k < 1 or k > 100:
    k = int(input("Please re-enter your stamina: "))

print("Please follow the key for each row:", key)
while i < n:
    print("Please enter the terrain for row", i+1)
    x = input()
    while j < len(x):
        if x[j] not in key:
            print("Please re-enter the terrain for row", i+1)
            x = input()
        elif len(x) != 5:
            print("Please re-enter the terrain for row", i+1)
            x = input()
        j = j + 1
    map.append(x)
    i = i + 1

i = 0
j = 0
while i < len(map):
    temp = []
    j = 0
    while j < len(map[i]):
        temp.append(map[i][j])
        j = j + 1
    i = i + 1
    grid.append(temp)

i = 0
while i < len(grid):
    j = 0
    while j < len(grid[i]):
        if grid[i][j] == ".":
            grid[i][j] = 1
        elif grid[i][j] == "F":
            grid[i][j] = 2
        elif grid[i][j] == "M":
            grid[i][j] = 3
        elif grid[i][j] == "#":
            grid[i][j] = 100
        j = j + 1
    i = i + 1

print(grid)
