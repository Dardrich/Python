ax = input().split()
ax = [i for i in ax]

a = int(ax[0])
x = int(ax[1])

if a < x:
    n = x//a
    m = x%a
elif a > x:
    n = 0
    m = x
else:
    n = 1
    m = 0

print(n,m)