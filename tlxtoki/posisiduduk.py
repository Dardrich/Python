mab = input().split()
mab = [int(i) for i in mab]
m = mab[0]
a = mab[1]
b = mab[2]
minmax = []

#kasus min
if (a%2 == 1) and (b%2 == 1) and (a+b == m*2):
    minmax.append(1)
else:
    minmax.append(0)

minmax.append(min(a,b))

for i in minmax:
    print(i,end=" ")
