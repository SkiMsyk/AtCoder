W, H, x, y = map(int, input().split())
if x * 2 == W and y * 2 == H:
    flg = 1
else:
    flg = 0
print(W*H/2, flg)