#Number Pattern using a loop

rows = int(input("Input number of rows: "))

for y in range(rows):
    for x in range(y + 1):
        print(x + 1)
    print()