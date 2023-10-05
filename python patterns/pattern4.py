rows = int(input("Enter the no.of rows: "))
b = 0
# reverse for loop from no.of rows to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
