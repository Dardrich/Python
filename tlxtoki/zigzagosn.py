n = int(input())
datas = []
contradict = []

for _ in range(n):
    nums = int(input())
    datas.append(nums)

for i in range(n-2):
    if datas[i]<=datas[i+1]<=datas[i+2] or datas[i]>=datas[i+1]>=datas[i+2]:
        contradict.append(datas[i])
        contradict.append(datas[i+1])
        contradict.append(datas[i+2])

if len(contradict) == 0:
    print("ZIGZAG")
else:
    print(contradict[0],contradict[1],contradict[2])
