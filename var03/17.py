nums = []
minimum = 10_000
sum_4 = 0
count_4 = 0
for i in open('17.txt'):
    n = int(i)
    nums.append(n)
    minimum = min(n, minimum)
    if n % 4 == 0:
        sum_4 += n
        count_4 += 1
mid_4 = sum_4 / count_4

ans_count = 0
ans_max = 0
for i in range(len(nums) - 1):
    if (nums[i] % minimum == 0 or nums[i + 1] % minimum == 0) and (nums[i] + nums[i + 1]) < mid_4:
        ans_count += 1
        ans_max = max(ans_max, nums[i] + nums[i + 1])
print(ans_count, ans_max)
