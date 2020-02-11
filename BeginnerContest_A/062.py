x, y =map(int, input().split())
groups = [
    [1,3,5,7,8,10,12],
    [4,6,9,11],
    [2]
    ]

res = 'No'
for g in groups:
    if x in g and y in g:
        res = 'Yes'

print(res)