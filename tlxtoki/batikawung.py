k,c,a = input().split()

if 2<=int(k)<=100:
    for i in range(int(k)):
        for j in range((int(k))):
            if i == j or i+j == int(k)-1:
                print(a,end="")
            else:
                print(c,end="")
        print()