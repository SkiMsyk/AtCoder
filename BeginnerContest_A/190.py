A, B, C = map(int, input().split())
if A == B:
    if C:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if A>B:
        print('Takahashi')
    else:
        print('Aoki')