n = 7
array = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            array[i][j] = 1
        else:
            array[i][j] = 0

print("Двовимірний масив:")
for row in array:
    print(" ".join(map(str, row)))
