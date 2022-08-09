# make dict
d = {}
for i in range(10):
    c = [i]
    while c[-1]*c[0] % 10 not in c:
        now = c[-1]*c[0] % 10
        c.append(now)
    d[i] = c

# input
A,B,C = map(int, input().split())

# calc
p = d[A % 10]
cycle = len(p)
rem = ((B % cycle) ** max(C % cycle, 1)) % cycle - 1
ams = p[rem]
print(ams)