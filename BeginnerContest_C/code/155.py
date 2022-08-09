n = int(input())
s = {}
for _ in range(n):
    si = input()
    if si not in s.keys():
        s[si] = 0
    else:
        s[si] += 1

maxvalue = max(s.values())
res = sorted([k for k,i in s.items() if i == maxvalue])
print('\n'.join(res))