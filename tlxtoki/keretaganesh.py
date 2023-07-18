n = int(input())

nums = input().split()
nums = [num for num in nums]

if n == len(nums):
    nums = nums[::-1]
    
for i in range(len(nums)):
    if i == len(nums) - 1:
        print(nums[i], end="")
    else:
        print(nums[i], end=",")
