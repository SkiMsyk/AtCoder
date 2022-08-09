# input
n,a,b,c = map(int,input().split())
l = [0]*n
for _ in range(n):
    l[_] = int(input())
    
# dfs
def dfs(d, choice):
    if d == n:
        return calc(choice)
    for i in range(4):
        choice[d] = i
        dfs(d+1,choice)

def calc(choice):
    global ans
    cost = 0
    for i,v in enumerate([a,b,c]):
        cand = [e[0] for e in zip(l, choice) if e[1] == i]
        if len(cand) == 0:
            cost = 10000
        else:
            cost += (len(cand)-1) * 10
            cost += abs(sum(cand) - v)
    if cost < ans:
        ans = cost

ans = 10000
dfs(0,[0]*n)
print(ans)
