n = int(input())

datas_main = []
datas_sekon = []

for _ in range(n):
    tasks = input().split()
    datas_sekon.append(tasks)

for i in range(n):
    a = datas_sekon[i][0]
    if len(datas_sekon[i]) > 1:
        b = datas_sekon[i][1]
        if b and 1 <= int(b) <= 1000000:
            if a == "push_front":
                datas_main.insert(0, b)
            elif a == "push_back":
                datas_main.append(b)
    else:
        if a == "pop_front":
            if len(datas_main) > 0:
                datas_main.pop(0)
            else:
                pass
        elif a == "pop_back":
            if len(datas_main) > 0:
                datas_main.pop()
            else:
                pass

for e in datas_main:
    print(e)



