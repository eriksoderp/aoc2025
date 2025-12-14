from functools import cache
graph = {row[0][:-1]: row[1:] for row in (line.split() 
                              for line in open('input11.txt').read().splitlines())}

@cache
def dfs(src, dest):
    if src == dest: return 1
    else: return sum(dfs(child, dest) for child in graph[src])

@cache
def dfs2(src, dest, fft_visited, dac_visited):
    if src == 'fft': fft_visited = True
    elif src == 'dac': dac_visited = True

    if src == dest: return int(fft_visited and dac_visited)
    else: return sum(dfs2(child, dest, fft_visited, dac_visited) for child in graph[src])

print("Part 1:", dfs('you', 'out'))
print("Part 2:", dfs2('svr', 'out', False, False))
