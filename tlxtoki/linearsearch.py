n, d = map(int, input().split())

print(next((i for i in range(n) if input() == str(d)), -1))

