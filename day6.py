from collections import defaultdict
from math import prod
lines = open('input6.txt').read().splitlines()

problems = defaultdict(list)
for line in lines[:-1]:
    for i, n in enumerate(line.split()):
        problems[i].append(int(n))

problems2 = defaultdict(list)
problem_index = 0
for line in zip(*lines[:-1]):
    if all(n == ' ' for n in line): 
        problem_index += 1
        continue
    
    problems2[problem_index].append(int(''.join(line)))

part1, part2 = 0, 0
sum_or_prod = lambda op, arr: sum(arr) if op == '+' else prod(arr)
for i, op in enumerate(lines[-1].split()):
    part1 += sum_or_prod(op, problems[i])
    part2 += sum_or_prod(op, problems2[i])

print("Part 1:", part1)
print("Part 2:", part2)
