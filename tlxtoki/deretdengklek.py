n = int(input())

if 1 <= n <= 100:
    numbers = [str(i) for i in range(1, n+1)]
    print('+'.join(numbers))
