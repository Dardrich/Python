nd = input().split()
nd = [int(i) for i in nd]

n = nd[0]
d = nd[1]

if (n >= 1) and (d <= 100):
    if n >= (d**10):
        print("NO")
    else:
        print("YES")