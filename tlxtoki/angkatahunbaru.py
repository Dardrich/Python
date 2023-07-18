n = int(input())

if n ==  1:
    print("NO")
elif 2 <= n < 7:
    data = []
    for i in range(1,int((n**0.5))+1):
        if n % i == 0:
            data.append(i)
    if len(data) == 1:
        print("YES")
    else:
        print("NO")
elif n >= 7:
    print("NO")
