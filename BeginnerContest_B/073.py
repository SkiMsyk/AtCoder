# Theater
# input
N = int(input())

# processing
total = 0
for _ in range(N):
    l, r = map(int, input().split())
    total += (r - l + 1)

# output
print(total)
