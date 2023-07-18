p,q,r = map(int, input().split())

for _ in range(int(input())):
    nums = int(input())
    if (nums%p)+(nums%q)+(nums%r) == 0:
        print("YA")
    else:
        print('TIDAK')