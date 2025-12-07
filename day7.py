from collections import defaultdict
grid = {(j, i): c for i, row in enumerate(open('input7.txt').readlines())
                  for j, c in enumerate(row.strip())}

starting_pos = next(pos for pos, c in grid.items() if c == 'S')
end_col, end_row = max(pos for pos in grid.keys())
beams = defaultdict(int)
beams[starting_pos[0]] = 1

count = 0
for row in range(end_row+1):
    for col in range(end_col+1):
        if col not in beams or beams[col] == 0: continue
        if grid.get((col, row)) == '^':
            beams[col-1] += beams[col]
            beams[col+1] += beams[col]
            beams[col] = 0
            count += 1

print("Part 1:", count)
print("Part 2:", sum(beams.values()))
