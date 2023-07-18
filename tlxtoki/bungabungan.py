pq = input().split()
pq = [int(num) for num in pq]

total = (pq[0]**2) + (pq[1]**2) + 1
if total % 4 == 0:
    print(total//4)
else:
    print("-1")