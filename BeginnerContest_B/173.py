# Judge Status Summary
N = int(input())
ans = {'AC':0, 'WA':0, 'TLE':0, 'RE':0}
for _ in range(N):
    s = input()
    ans[s] += 1
for k,v in ans.items():
    print(k + ' x ' + str(v))
