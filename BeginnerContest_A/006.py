N = int(input())
if N % 3 == 0 or "3" in [e for e in str(N)]:
    print("YES\n")
else:
    print("NO\n")