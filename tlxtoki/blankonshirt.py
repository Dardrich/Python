b,p,l = map(int,input().split())

if b<=10 and p<=40 and l<=90:
    print("S")
elif b<=14 and p<=60 and l<=120:
    print('M')
elif b<=18 and p<=80 and l<=180:
    print("L")
else:
    print('X')