A, B, C = map(int, input().split())
ans = ['Yes', 'No'][A**2 + B**2 >= C**2]
print(ans)
