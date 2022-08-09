N,M,X,T,D = map(int,input().split())
BASE_HEIGHT = T - D*X
ans = min(M*D, X*D) + BASE_HEIGHT
print(ans)