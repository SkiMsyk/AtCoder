def max_pop(a):
    return a.pop(a.index(max(a)))

def CardGameForTwo(N, a):
    """
    a include N integers.
    Alice and Bob will do game.
    1. each player pull a card from a.
    2. Alice will be first.
    3. When all cords were pull, the game end.
    4. calculate sum of card numbers
    5. if Alice and Bob take a strategy that is maxmization of it`s total number as soon as possible,
    how much difference of two numbers?
    """
    Alice = []
    Bob = []
    turn = 'Alice'
    for i in range(N):
        if turn == 'Alice':
            Alice.append(max_pop(a))
            turn = 'Bob'
        else:
            Bob.append(max_pop(a))
            turn = 'Alice'
    return sum(Alice) - sum(Bob)

N = int(input())
a = list(map(int, input().split()))

res = CardGameForTwo(N=N, a=a)
print(res)
