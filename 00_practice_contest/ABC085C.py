def Otoshidama(N, total):
    for i in range(N+1):
        res = [0,0,0]
        res[0] = i
        if total == 10000*i and i == N:
            return res
        for j in range(N-i+1):
            res[1] = j
            if total == (10000*i + 5000*j + 1000*(N-(i+j))):
                res[2] = (N-(i+j))
                return res
            else:
                continue
    return [-1, -1, -1]

def main():
    N, total = map(int, input().split())
    res = Otoshidama(N=N, total=total)
    print("{} {} {}".format(res[0], res[1], res[2]))

main()