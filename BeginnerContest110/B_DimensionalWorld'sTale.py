n,m,x,y = map(int, input().split())
px = list(map(int, input().split()))
py = list(map(int, input().split()))
# import ipdb; ipdb.set_trace()
if max(px) < min(py) and (x+1) < y and max(px) < y and x < min(py) :
    for z in range(x+1, y+1):
        if z in range(max(px), min(py)+1):
            print('No War')          
            break
    else:
        print('War')
else:
    print('War')