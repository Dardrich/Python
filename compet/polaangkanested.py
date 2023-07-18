def generate_pattern(n):
    num = 0
    for i in range(1, n+1):
        pattern = ""
        for j in range(i):
            pattern += str(num)
            num = (num + 1) % 10
        print(pattern)

n = int(input())
generate_pattern(n)
