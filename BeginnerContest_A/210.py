# X: unit price
# Y: special price
# A: <= A -> unit price,  >= A+1 -> special price
# N: the number you need
N,A,X,Y=map(int,input().split())
ans = min(N, A) * X + max(0, N - (A)) * Y
print(ans)