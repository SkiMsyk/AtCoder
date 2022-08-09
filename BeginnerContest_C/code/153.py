n,k = map(int, input().split())
h = [0] + sorted(list(map(int,input().split())))
print(sum(h[:max(0, (n-k+1))]))