import numpy as np

H, W = map(int, input().split())
field = []
for i in range(H):
    field.append(list(map(int, input().split())))

rd = [(0,1,0), (1,0,1)]

move_records = []

if H != 1 or W != 1:
    for i in range(H):
        for j in range(W):
            if field[i][j] % 2 == 0:
                continue
            if i == H-1 and j == W-1:
                continue
            if i == H-1 and j == W-2:
                # import ipdb; ipdb.set_trace()
                if (field[H-1][W-1] + field[H-1][W-2]) % 2 != 0:
                    continue
                else:
                    field[H-1][W-2] -= 1
                    field[H-1][W-1] += 1
                    move_records.append([i+1,j+1,i+1,j+2])

            elif j != W-1:
                field[i][j] -= 1
                field[i][j+1] += 1
                move_records.append([i+1,j+1,i+1,j+2])
            else:
                field[i][j] -= 1
                field[i+1][j] += 1
                move_records.append([i+1,j+1,i+2,j+1])

            # adj_values = np.array([-1, -1])
            # if not j == W-1:
            #     adj_values[0] = field[i][j+1]
            # if not i == H-1:
            #     adj_values[1] = field[i+1][j]



            # if sum(adj_values[adj_values != -1] % 2) == 0:
            #     h,w,k = rd[np.where(adj_values != -1)[0][0]]
            #     field[i][j] -= 1
            #     field[i+h][j+w] += 1
                
            # else:
            #     for h,w,k in rd:
            #         if adj_values[k] == -1:
            #             continue

            #         if adj_values[k] % 2 != 0:
            #             field[i][j] -= 1
            #             field[i+h][j+w] += 1
            #             break
            
            # move_records.append([i+1,j+1,i+h+1,j+w+1])

M = len(move_records)
print(M)
for i in range(M):
    print('{} {} {} {}'.format(move_records[i][0],
                               move_records[i][1],
                               move_records[i][2],
                               move_records[i][3]))