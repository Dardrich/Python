n = int(input())

datas = []

for _ in range(n):
    nums = input()
    datas.append(nums)

for data in datas:
    reversed_data = data[::-1]
    l = len(reversed_data)
    k = 0
    
    while k < l - 1 and reversed_data[k] == '0':
        k += 1

    if k == l - 1 and reversed_data[k] == '0':
        print('0')
    else:
        print(reversed_data[k:])
