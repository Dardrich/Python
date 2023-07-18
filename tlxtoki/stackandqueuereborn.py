a = []

for i in range(int(input())):
    x = input().split()
    if x[0] == "push_front":
        a.insert(0,x[1])
    elif x[0] == "push_back":
        a.append(x[1])
    elif x[0] == "pop_front":
        a.pop(0)
    elif x[0] == "pop_back":
        a.pop()

for i in a:
    print(i)