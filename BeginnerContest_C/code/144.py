def get_divisors(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n//i)
    return sorted(res)
    
N = int(input())
ds = get_divisors(N)

res = 10**12

if len(ds) % 2 != 0:
    # 平方数の場合
    for i in range((len(ds)+1) // 2):
        res = min(res, ds[i] + ds[-(i+1)])
else:
    # 平方数でない場合
    for i in range(len(ds) // 2):
        res = min(res , ds[i] + ds[-(i+1)])
        
print(res - 2)