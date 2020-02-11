# Trained?

# input
N = int(input())
a = [int(input()) for _ in range(N)]
shining = a[0]
flag = False
for _ in range(1, N):
    if shining == 2:
        flag = True
        break
    shining = a[shining-1]

if flag:
    print(_)
else:
    print(-1)