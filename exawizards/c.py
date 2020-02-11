N, Q = map(int, input().split())
s = input()
ts = list()
ds = list()
for _ in range(N):
    t, d = input().split()
    ts.append(t)
    ds.append(d)


flag_L = True
flag_R = True
l = 0
r = N-1
while flag_L or flag_R:
    for ft, fd, bt, bd in zip(ts, ds, ts[-1::-1], ds[-1::-1]):
        