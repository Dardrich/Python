ab = input().split()

ab = [int(i) for i in ab]

if 1 <= ab[0] <= 100 and 1 <= ab[1] <= 100:
    print(ab[0]+ab[1])
    print(ab[0]-ab[1])
    print(ab[0]*ab[1])
    print(ab[0]//ab[1])
    print(ab[0]%ab[1])
