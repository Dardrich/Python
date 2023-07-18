data1 = input()
data2 = data1.split()

n = int(data2[0])
k = int(data2[1])

for i in range(1,n+1):
    if i % k == 0:
        print("*", end=" ")
    else:
        print(i, end=" ")