W, H, x, y = map(int, input().split())

# xで分割する場合
xres = min((W-x)*H, W*H - (W-x)*y)

# yで分割する場合
yres = min(W*(H-y), W*H - x*(H-y))

check = 1 if xres == yres else 0

print(W*H/2, check)