def main():
    N = int(input())
    d = []
    iter = 0
    while iter < N:
        d.append(int(input()))
        iter += 1
    res = set(d)
    print(len(res))

main()
