N = int(input())
H = list(map(int, input().split()))
res = 'Yes'
for i in range(N-1):
    if H[i] < H[i+1]:
        H[i+1] -= 1
    elif H[i+1] - H[i] == 0:
        continue
    else:
        res = 'No'
        break
print(res)