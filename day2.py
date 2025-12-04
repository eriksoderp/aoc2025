from collections import defaultdict
from math import floor, log10
ranges = [r.split('-') for r in open('input2.txt').read().split(',')]
nums = defaultdict(list)
for a, b in ranges:
    for i in range(int(a), int(b)+1):
        nums[floor(log10(i)) + 1].append(i)

periods = defaultdict(list)
for l in range(2, max(nums.keys())+1):
    for p in range(1, l // 2 + 1):
        if l % p != 0: continue
        period = sum(10 ** power for power in range(0, l - p + 1, p))
        periods[l].append((p, period))

def calculate_sum(part1, periods):
    count = 0
    for l, periods in periods.items():
        for num in nums[l]:
            for p, period in periods:
                if part1 and l // p != 2: continue
                if num % period == 0:
                    count += num
                    break
    return count

print("Part 1:", calculate_sum(part1=True, periods=periods))
print("Part 2:", calculate_sum(part1=False, periods=periods))
