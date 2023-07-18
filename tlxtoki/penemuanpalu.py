xy = input().split()
xy = [int(i) for i in xy]

x = xy[0]
y = xy[1]

if x >= y:
    print("YES")
else:
    print("NO")