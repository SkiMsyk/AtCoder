def solve(N):
    k = len(N)
    n = int(N)
    if k == 1:
        print(0)
    else:
        res = 0
        k = k // 2
        for i in range(10**(k-1), 10**k):
            cand = int(str(i) + str(i))
            if cand <= n:
                res += 1

        k -= 1
        while k != 0:
            res += 10**k - 10**(k-1)
            k -= 1
        print(res)
    

if __name__ == '__main__':
    N = input()
    solve(N)