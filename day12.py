from re import findall
parts = open('input12.txt').read().split('\n\n')
pieces = {int(part[0]): (part.split('\n')[1:], part.count('#')) for part in parts[:-1]}

regions = parts[-1].split('\n')
fits = 0
for region in regions:
    nums = [int(num) for num in findall(r'\d+', region)]
    space = nums[0]*nums[1]
    pieces_to_fit = [pieces[j] for j in range(len(nums[2:])) for _ in range(nums[j+2])]
    if space >= sum(piece[1] for piece in pieces_to_fit): fits += 1
    
# Tried to minimize the problem by keeping the ones with sufficient space first
# Turned out to be the correct answer
print("Part 1:", fits)
