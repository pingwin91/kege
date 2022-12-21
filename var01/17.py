f = open('17.txt')

nums = []
for i in f:
    nums.append(int(i))

count = 0
max_mult = -1_000_001
for i in range(len(nums) - 1):
    if nums[i] + nums[i + 1] > 100 and (nums[i] < 0 or nums[i + 1] < 0):
        count += 1
        max_mult = max(max_mult, nums[i] * nums[i + 1])
print(count)
print(max_mult)
