n = int(input("Please enter the number of rows: ")) # num of rows
m = int(input("Please enter the number of columns: ")) # num of columns
k = int(input("Please enter your stamina: ")) # stamina
i = 0
j = 0
map = []
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

print(map[0]) # TEMP LINE REMOVE FROM FINAL CODE
print(map[1]) # TEMP LINE REMOVE FROM FINAL CODE

i = 0
j = 0
while i < len(map[j]):
    row1 = []
    x = map[0]
    

# Converting the key to their respective stamina cost (may be unnecessary)
key[0] = 1 # start
key[1] = 1 # plains
key[2] = 2 # forest
key[3] = 3 # mountain
key[4] = 100 # river (unpassable)
key[5] = 1 # treasure
