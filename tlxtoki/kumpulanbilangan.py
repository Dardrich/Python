n = int(input())

datas_neg = []
datas_zero = []
datas_pos = []

for _ in range(n):
    nums = int(input())
    
    if nums<0:
        datas_neg.append(nums)
    elif nums>0:
        datas_pos.append(nums)
    else:
        datas_zero.append(nums)

for j in datas_neg:
    print(j)
for l in datas_zero:
    print(l)
for k in datas_pos:
    print(k)


