ranges, ids = open('input5.txt').read().split('\n\n')
fresh_ranges = [range(int(a), int(b)+1) for a, b in (r.split('-')
                                        for r in ranges.split('\n'))]

print("Part 1:", sum(any(int(id) in r for r in fresh_ranges)
                                      for id in ids.split('\n'))) 

fresh_ranges.sort(key=lambda x: x[0])
merged_ranges = [fresh_ranges[0]]
for r in fresh_ranges[1:]:
    if r[0] in (mr := merged_ranges[-1]):
        merged_ranges[-1] = range(mr[0], max(mr[-1], r[-1])+1)
        continue

    merged_ranges.append(r)

print("Part 2:", sum(r[-1] - r[0] + 1 for r in merged_ranges))
