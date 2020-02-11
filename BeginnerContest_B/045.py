SA = input()
SB = input()
SC = input()

turn = 'a'

while True:
    if turn == 'a':
        if len(SA) == 0:
            res = 'A'
            break
        turn = SA[0]
        SA = SA[1:]
    elif turn == 'b':
        if len(SB) == 0:
            res = 'B'
            break
        turn = SB[0]
        SB = SB[1:]
    elif turn == 'c':
        if len(SC) == 0:
            res = 'C'
            break
        turn = SC[0]
        SC = SC[1:]

print(res)