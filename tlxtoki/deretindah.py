snd = input().split()
snd = [int(i) for i in snd]

s = snd[0]
n = snd[1]
d = snd[2]
data = []

for en in range(n):
    s += d
    data.append(s-d)
for datas in data:
    print(datas)
