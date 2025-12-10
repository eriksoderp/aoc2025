from re import findall
from collections import defaultdict
from heapq import heappop, heappush
from z3 import *
machines = [line.split() for line in open('input10.txt').read().splitlines()]

def create_button(machine_length, button):
    button = list(map(int, findall(r'-?\d+', button)))
    return [1 if i in button else 0 for i in range(machine_length)]

def press_button(lights, button):
    return [l ^ b for l, b in zip(lights, button)]

def dijkstra_part1(desired_lights, buttons):
    lights = [0 for _ in range(len(desired_lights))]
    q = [(0, tuple(lights))]
    costs = defaultdict(lambda: float('inf'))
    costs[tuple(lights)] = 0

    while q:
        cost, current_lights = heappop(q)
        if current_lights == tuple(desired_lights): break
        if cost > costs[current_lights]: continue
        for button in buttons:
            new_lights = tuple(press_button(current_lights, button))
            new_cost = cost + 1
            if new_cost < costs[new_lights]:
                costs[new_lights] = new_cost
                heappush(q, (new_cost, new_lights))
    
    return costs[tuple(desired_lights)]

def solve_linear_equation(desired_joltages, buttons):
    opt = Optimize()
    vars = Ints(' '.join(f'x{i}' for i in range(len(buttons))))
    for i, joltage in enumerate(desired_joltages):
        constraint = Sum([button[i]*var for button, var in zip(buttons, vars)]) == joltage
        opt.add(constraint)

    for var in vars: opt.add(var >= 0)
        
    opt.minimize(Sum(vars))
    if opt.check() == sat:
        model = opt.model()
        return model.eval(Sum(vars)).as_long()
    return -1
    
p1, p2 = 0, 0
for machine in machines:
    desired_lights = [0 if c == '.' else 1 for c in machine[0] if c not in '[]']
    buttons = [create_button(len(desired_lights), button) for button in machine[1:-1]]
    desired_joltages = [int(c) for c in findall(r'-?\d+', machine[-1])]
    p1 += dijkstra_part1(desired_lights, buttons)
    p2 += solve_linear_equation(desired_joltages, buttons)
    
print("Part 1:", p1)
print("Part 2:", p2)
