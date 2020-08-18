# Mix Juice
N,K = map(int,input().split())
p = sorted(list(map(int, input().split())))
ans = sum(p[:K])
print(ans)
