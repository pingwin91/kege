with open('17.txt') as f:
    max_eq_11 = 0
    nums = []
    for i in f:
        number = int(i)
        nums.append(number)
        if number % 11 == 0:
            max_eq_11 = max(max_eq_11, number)

count = 0
max_sum = 0
for i in range(len(nums) - 1):
    if (nums[i] % 11 == 0 or nums[i + 1] % 11 == 0) and (nums[i] + nums[i + 1] <= max_eq_11):
        count += 1
        max_sum = max(max_sum, nums[i] + nums[i + 1])
print(count, max_sum)

# 731 990