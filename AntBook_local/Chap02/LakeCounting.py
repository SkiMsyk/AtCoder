n = int(input())
m = int(input())
field = [list(input()) for _ in range(n)]

# direction
# 適当なWから初めて，そこから繋がっている部分を.に置き換える操作を繰り返す
# 1回のdfsで最初のWと繋がっているWは全て.に置き換わるので，Wがなくなるまで
# 何回DFSを実行したかが答えとなる
# この時，計算量はO(8xNxM)

def dfs(x, y):
    # 今いるところを置き換える
    field[x][y] = '.'
    
    # 移動する8方向をループさせる
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            # x方向への移動をdx, y方向への移動をdyとする
            nx = x + dx
            ny = y + dy

            # (nx, ny)が庭の範囲内かどうかとfield[nx][ny]が水溜りかどうかを判定する
            if 0 <= nx and nx < n and 0 <= ny and ny < m and field[nx][ny] == "W":
                dfs(nx, ny)

res = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == "W":
            dfs(i,j)
            for i in range(n):
                print(''.join(field[i]))
            print('---')
            res += 1

print(res)