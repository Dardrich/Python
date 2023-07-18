datas = []
for _ in range(3):
    n = input()
    datas.append(n)

k = int(datas[0])
c = datas[1]
d = datas[2]

div = ((k//2)+1)

if k % 2 == 1:
    for i in range(1,k+1):
        for j in range(1,k+1):
            if j == 1 or j == k:
                print(d,end="")
            elif i == 1 or i == k:
                print(d,end="")
            elif i == div and j == div:
                print("*",end="")
            else:
                print(c,end="")
        print()
else:
    for i in range(1,k+1):
        for j in range(1,k+1):
            if j == 1 or j == k:
                print(d,end="")
            elif i == 1 or i == k:
                print(d,end="")
            else:
                print(c,end="")
        print()
