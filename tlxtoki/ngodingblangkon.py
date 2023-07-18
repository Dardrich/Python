abck = list(map(int, input().split()))
a, b, c, k = abck[:4]

datas = [a, b, c]

if k == 1:
    sorted_datas = sorted(datas)
elif k == 0:
    sorted_datas = sorted(datas, reverse=True)

for i in sorted_datas:
    print(i, end=" ")
