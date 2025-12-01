rows = [(r[0], int(r[1:])) for r in open('input1.txt').read().split('\n')]
pos, part1, part2 = 50, 0, 0
for rot, steps in rows:
    if steps >= 100:
        part2 += steps // 100
        steps = steps % 100
    if rot == 'R':
        if pos + steps >= 100: part2 += 1
        pos += steps
    else:
        if pos - steps <= 0 and pos > 0: part2 += 1
        pos -= steps
    
    pos = pos % 100
    if pos == 0: part1 += 1
    
print("Part 1:", part1)
print("Part 2:", part2)
