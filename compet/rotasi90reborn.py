n, m = map(int, input().split())

matriks = []
for _ in range(n):
    row = list(map(int, input().split()))
    matriks.append(row)

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        print(matriks[i][j], end=" ")
    print()
