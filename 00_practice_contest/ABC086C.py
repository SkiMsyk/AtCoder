def Traveling(N, T):
    i = 0
    res = 'Yes'
    while i < (len(T)-1):
        dt = T[i+1][0] - T[i][0]
        dx = abs(T[i+1][1] - T[i][1])
        dy = abs(T[i+1][2] - T[i][2])
        dd = dx + dy
        if dd > dt or (dt-dd)%2 != 0:
            res =  'No'
        i += 1
    return res

def main():
    T = [[0,0,0]]
    N = int(input())
    for i in range(N):
        T.append(list(map(int, input().split())))
    res = Traveling(N=N, T=T)
    print(res)

main()