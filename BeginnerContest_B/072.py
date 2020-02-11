# input
s = input()

# processing
res = [s[i] for i in range(len(s)) if (i + 1) % 2 != 0]

# output
print(''.join(res))