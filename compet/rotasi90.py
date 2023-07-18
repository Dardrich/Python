n,m = map(int,input().split())
matriks = []

for _ in range(n):
    i = list(map(int,input().split()))
    for j in i:
        matriks.append(j)

matriks = matriks[::-1]

for k in range(m-1,-1,-1):
    for l in range(0,len(matriks)):
        if l%m == k:
            print(matriks[l],end=" ")
    print()