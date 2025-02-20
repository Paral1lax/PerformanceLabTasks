import sys
file = sys.argv[1]
with open(file, encoding="utf-8") as f:
    lines = f.readlines()
nums = list(map(int, lines))
nums.sort()
median = nums[len(nums)//2]

steps = 0
for i in nums:
    steps += abs(median - i)
print(steps)