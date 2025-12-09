from shapely import Polygon
coords = [tuple(map(int, line.strip().split(','))) for line in open('input9.txt').readlines()]

area = lambda p, q: (abs(p[0]-q[0])+1) * (abs(p[1]-q[1])+1)
areas = [(p, q, a) for i, p in enumerate(coords) for q in coords[i+1:] if (a := area(p, q)) > 1]
areas.sort(key=lambda x: x[2], reverse=True)
poly = Polygon(coords)

print("Part 1:", areas[0][2])
print("Part 2:", next(a for p, q, a in areas
                        if poly.contains(Polygon([p, (p[0], q[1]), q, (q[0], p[1])]))))
