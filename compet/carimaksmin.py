n = int(input())
x = list(map(int,input().split()))

a,b = -10**6,10**6
for i in range(n):
    if a<x[i]:
        a = x[i]
    elif b>x[i]:
        b = x[i]
print(a,b)