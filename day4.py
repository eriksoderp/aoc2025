grid = {complex(j, i): c for i, row in enumerate(open('input4.txt').readlines())
                         for j, c in enumerate(row.strip())}
dirs = [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]
def find_accessible(part1):
    accessible = set()
    found = 0
    while True:
        for pos, c in grid.items():
            if c == '@':
                count = 0
                for d in dirs:
                    if count >= 4: break
                    if grid.get(pos + d) == '@': count += 1
                    
                if count < 4:
                    accessible.add(pos)
                    if not part1: grid[pos] = '.'

        if part1 or len(accessible) == found: break
        found = len(accessible)

    return len(accessible)

print("Part 1:", find_accessible(part1=True))
print("Part 2:", find_accessible(part1=False))
