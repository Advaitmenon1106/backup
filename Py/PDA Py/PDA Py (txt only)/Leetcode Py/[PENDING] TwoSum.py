# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = list(map(int,input().split()))
target = int(input())
output = []
length = len(nums)
for x in range (0, length):
    for y in range (0, length):
        if nums[x]+nums[y] == target:
            output.append(x)
            output.append(y)
print (output)
