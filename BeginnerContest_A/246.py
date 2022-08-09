# input
points = []
xs = set()
ys = set()
for i in range(3):
    input_new = list(map(int, input().split()))
    xs.add(input_new[0])
    ys.add(input_new[1])
    points.append(input_new)

# solution
xs = list(xs)
ys = list(ys)

candidates = [
    [xs[0], ys[0]],
    [xs[0], ys[1]],
    [xs[1], ys[0]],
    [xs[1], ys[1]]
]

missing_point = [ e for e in candidates if e not in points]
print(' '.join([str(e) for e in missing_point[0]]))