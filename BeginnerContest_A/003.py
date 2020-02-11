N = int(input())
res = sum([(10000*i)/N for i in range(1, N+1)])
print(int(res))