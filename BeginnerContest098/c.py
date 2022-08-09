n=int(input())
s=list(input())
p=s.count('E')
ans=p
for i in s:
    if i=="E":
        p-=1
    else:
        p+=1
    ans=min(p,ans)
print(ans)

# これは写経なのでsubmitしてないが
# 中身を理解できたので写して置く．
# 頭良い