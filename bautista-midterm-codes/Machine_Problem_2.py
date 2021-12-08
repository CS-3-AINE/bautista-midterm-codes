#Number Pattern using a loop

rows  = int(input("Input number of rows: "))

for y in range(rows, 4, -1):
    for x in range(1, y + 1):
        print("#", end = " ")
    print()