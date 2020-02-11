n, x = map(int, input().split())

bn = 'p'
for i in range(1,n+1):
    bn = 'b' + bn + 'p' + bn + 'b'

res = sum([True for s in bn[-1:len(bn)=:-1] if s == 'p'])

print(bn)
print(res)