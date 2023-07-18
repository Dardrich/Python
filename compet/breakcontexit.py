nums = int(input())

for num in range(nums):
    if (num % 10 == 9):
        continue
    elif num == 41:
        print("ERROR")
        exit()
    print(num+1)