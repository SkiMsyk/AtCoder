# input
N = int(input())
A = list(map(int, input().split()))

# solution
counter = 0
while sum([e < 2 for e in A]) == 0:
    if sum([e % 2 for e in A]) == 0:
        counter += 1
        A = [e // 2 for e in A]
    else:
        break
    
# output
print(counter)