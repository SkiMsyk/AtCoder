A = int(input())
B = int(input())
C = int(input())
X = int(input())

def test():
    # initialize counter
    n = 0

    for i in range(A+1):
        # 500円を1枚ずつ払って行く
        X2 = X - 500 * i
        if X2 < 0:
            continue
        elif X2 == 0:
            n += 1
        else:
            for j in range(B+1):
                X3 = X2 - 100*j
                if X3 < 0:
                    continue
                elif X3 == 0:
                    n += 1
                else:
                    for k in range(C+1):
                        X4 = X3 - 50*k
                        if X4 == 0:
                            n += 1
    return n

if __name__ == '__main__':
    n = test()
    print(n)