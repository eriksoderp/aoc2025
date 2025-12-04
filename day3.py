rows = open('input3.txt').read().splitlines()
def find_max_rec(n, bank):
    if n == 0: return ''
    max = 0
    for index, i in enumerate(bank):
        if len(bank) - n < index: continue
        if int(i) > max:
            max = int(i)
            max_index = index

    return str(max) + find_max_rec(n-1, bank[max_index+1:])

print("Part 1: ", sum(int(find_max_rec(2, r)) for r in rows))
print("Part 2: ", sum(int(find_max_rec(12, r)) for r in rows))
