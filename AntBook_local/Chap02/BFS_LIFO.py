from queue import LifoQueue

n,m = map(int, input().split())
maze = [list(input()) for _ in range(m)]
sx,sy = map(int, input().split())
gx,gy = map(int, input().split())

d = [[0]*m for _ in range(n)]

p = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs_lifo():
    q = LifoQueue() # まだ探索してない場所のキュー
    q.put([sx, sy])
    d[sx][sy] = 1
    # queが空になるまでループ
    while q.empty() != True:
        # qの先頭を取り出す
        current_x, current_y = q.get()
        # if p[0] == gx and p[1] == gy:
        #     break
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]

            if 0 <= nx and nx < n and 0 <= ny and ny < m:
                if maze[nx][ny] != '#' and d[nx][ny] == 0:
                    q.put([nx,ny])
                    # 上下左右に隣り合うますの中で０でない最小の数から１を足した数が最小経路
                    previous_number = []
                    if 0 <= nx - 1:
                        previous_number.append(d[nx-1][ny])
                    if nx + 1 < n:
                        previous_number.append(d[nx+1][ny])
                    if 0 <= ny - 1:
                        previous_number.append(d[nx][ny-1])
                    if ny + 1 < m:
                        previous_number.append(d[nx][ny+1])
                    minimum_length = min([e for e in previous_number if e != 0])
                    d[nx][ny] = minimum_length + 1
    return d

res = bfs()
print(res)