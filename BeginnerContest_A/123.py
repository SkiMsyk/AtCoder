# input
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# k = int(input())
a = [int(input()) for _ in range(5)]
k = int(input())

# solution
if max(a) - min(a) > k: res = ':('
else: res = 'Yay!'

# output
print(res)