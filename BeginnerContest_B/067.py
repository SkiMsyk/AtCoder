# Snake Toy

# input
N, K = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse = True)


# output
print(sum(l[:K]))

