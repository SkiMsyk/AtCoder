# (ai, bi) is red point value
# (ci, di) is blue point value
# if x axis value of red(ai) is smaller than x axis value of blue(ci)
# and y axis value of red(bi) is smaller than y axis value of blue(di)
# then red point and blue point will make good relation. 
# How many friend pairs? (a point will not be able to belong to two or more pairs.) 

n = int(input())
red = [list(map(int, input().split())) for _ in range(n)]
blue = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[0])

def beFriend(red, blue):
    if red[0] < blue[0] and red[1] < blue[1]:
        return 1
    else:
        return 0

res = 0

for b in blue:
    for r in sorted([sr for sr in red if sr[0] < b[0]], key=lambda x:x[1], reverse = True):
        if beFriend(r, b):
            res += 1
            red.pop(red.index(r))
            break

print(res)