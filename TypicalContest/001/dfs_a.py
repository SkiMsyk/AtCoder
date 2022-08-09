import sys
sys.setrecursionlimit(10**7)

H,W = map(int,input().split())
c = [['']*W]*H

for _ in range(H):
    nc = list(input())
    c[_] = nc
    if 's' in nc:
        s = (_, nc.index('s')) # startの位置
    if 'g' in nc:
        g = (_, nc.index('g')) # goalの位置
    

def dfs(x,y):
    # print(x,y)
    if (x < 0) or (x >= W) or (y < 0) or (y >= H) or (c[y][x] == '#') or (c[y][x] == 1):
        return     
    c[y][x] = 1
    
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

dfs(s[1], s[0])

print(['No','Yes'][c[g[0]][g[1]]==1])
