W, H, N = map(int, input().split())
ws, we, hs, he = 0, W, 0, H
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        ws = max(ws, x)
    elif a == 2:
        we = min(we, x)
    elif a == 3:
        hs = max(hs, y)
    elif a == 4:
        he = min(he, y)
if we >= ws and he >= hs:
    res = (we - ws)*(he - hs)
else:
    res = 0
print(res)